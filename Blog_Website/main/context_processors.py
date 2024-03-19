from django.contrib import messages
from datetime import date
from contact_us.models import ContactInfo
from marketing.utils import Mailchimp
from marketing.models import Marketing, GuestMarketing
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory
from posts.models import Post
from datetime import datetime, timedelta
from contact_us.models import ContactInfo
from main.models import SocialPages
from accounts.models import Account

def contexts(request):
    info = ContactInfo.objects.all()
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    contact_info = ContactInfo.objects.all().first()
    social_pages = SocialPages.objects.all().first()
    footer_last_posts = Post.objects.filter(is_published=True).order_by('-date','-time')[:3]
    this_week=(datetime.today() - timedelta(days=30))
    footer_most_views_posts = Post.objects.filter(timestamp__gte=this_week,is_published=True).order_by('-views_count')[:3]
    footer_most_like_posts = Post.objects.filter(timestamp__gte=this_week,is_published=True).order_by('-likes')[:3]
    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
        account.last_activity = datetime.now()
        account.save()

    if 'submit_footer_subscribe' in request.POST:    
        subscribe_email = request.POST.get('eamil_subscribe',None)
        if len(subscribe_email) != 0:
            email = Marketing.objects.filter(user__email=subscribe_email).first()
            if email is not None:
                if subscribe_email != email.user.email: 
                    guest_email, guset_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                    if guset_created:
                        Mailchimp().add_email(subscribe_email)
                        messages.success(request, 'ایمیل شما با موفقیت ثبت شد')                
                else:   
                    messages.error(request, 'ایمیل شما قبلا ثبت شده است')
            else:
                guest_email, guset_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                if guset_created:
                    Mailchimp().add_email(subscribe_email)
                    messages.success(request, 'ایمیل شما با موفقیت ثبت شد')                
                else:   
                    messages.error(request, 'ایمیل شما قبلا ثبت شده است')
                    
    context = {
        'info' : info.first(), 
        'cat' : cat,
        'subcat' : subcat, 
        'social_pages' : social_pages,
        'contact_info' : contact_info,
        'footer_last_posts' : footer_last_posts,
        'footer_most_views_posts' : footer_most_views_posts,
        'footer_most_like_posts' : footer_most_like_posts,
    }
       
    return(context)