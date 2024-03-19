from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from posts.models import Post
from categories.models import Category
from subcategories.models import Subcategory
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import Account
from datetime import datetime, timedelta

def home(request):
    post = Post.objects.filter(is_published=True).order_by('-date','-time')
  
    paginator = Paginator(post,8)    
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    lastposts = Post.objects.filter(is_published=True).order_by('-date','-time')[:6]

    this_week=(datetime.today() - timedelta(days=30))
    popular_posts = Post.objects.filter(timestamp__gte=this_week,is_published=True).order_by('-likes')[:8]
    most_visited_posts = Post.objects.filter(timestamp__gte=this_week,is_published=True).order_by('-views_count')[:8]
    most_comment_posts = Post.objects.filter(timestamp__gte=this_week,is_published=True,comments_count__gte=1).order_by('-comments_count')[:4]

    subcategory_trends = Subcategory.objects.all().annotate(qs_posts=Count('posts')).order_by('-qs_posts')[:3]

    post_trend_list = []
    for i in subcategory_trends:
        post_trend = Post.objects.filter(subcategory__id=i.id)[:3]
        post_trend_list.append(post_trend)

    trends = zip(subcategory_trends,post_trend_list)
    context ={  
                'posts':paged_posts,
                'all_posts': post,
                'cat':cat, 
                'subcat':subcat, 
                'lastposts':lastposts, 
                'popular_posts':popular_posts, 
                'most_visited_posts':most_visited_posts,
                'trends':trends,
                'most_comment_posts':most_comment_posts,                
      }
    return render(request, 'front/home.html', context)

