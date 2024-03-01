from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Subcategory
from categories.models import Category
from posts.models import Post

@login_required
def staff_subcategory_list(request):
    if not request.user.profile_user.is_writer and not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        subcategory = Subcategory.objects.all()
        paginator = Paginator(subcategory,10)    
        page = request.GET.get('page')
        paged_subcategory = paginator.get_page(page)

        context = {
            'subcategories':paged_subcategory,
        }

        return render(request, 'staff-panel/subcategory-list.html',context)


@login_required
def staff_subcategory_add(request):
    if not request.user.profile_user.is_writer and not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        categories = Category.objects.all()
        if request.method == 'POST':
            title = request.POST.get('title')
            main_cat = request.POST.get('main-cat')
            image_alt = request.POST.get('image-alt')
            print(main_cat)
            if title == "" :

                messages.error(request, 'یک نام برای دسته بندی انتخاب کنید')
                return redirect('staff-subcategory-add')

            if not main_cat :

                messages.error(request, 'دسته بندی اصلی را مشخص کنید')
                return redirect('staff-subcategory-add')

            if len(Subcategory.objects.filter(title=title)) != 0 :

                messages.error(request, 'دسته بندی مورد نظر از قبل موجود است')
                return redirect('staff-subcategory-add')

            try:
            
                myfile = request.FILES['image']
        
                if str(myfile.content_type).startswith("image"):

                    if myfile.size < 5000000 :    
                        main_cat = Category.objects.get(title=main_cat)          
                        subcategory_add = Subcategory.objects.create(title=title,image=myfile,image_alt=image_alt,main_cat=main_cat)
                        if request.POST.get('save_and_return'):
                            return redirect('staff-subcategory-list')
                        elif request.POST.get('save_and_another'):
                            return redirect('staff-subcategory-add')

                    else:

                        messages.error(request, 'تصویر انتخاب شده باید کمتر از 5 مگابایت باشد')
                        return redirect('staff-subcategory-add')

                else:

                    messages.error(request, 'فرمت فایل انتخاب شده برای تصویر پشتیبانی نمیشود')
                    return redirect('staff-subcategory-add')

            except:

                messages.error(request, 'تصویری را برای دسته بندی انتخاب کنید')
                return redirect('staff-subcategory-add')

        return render(request, 'staff-panel/subcategory-add.html',{'categories':categories})


@login_required
def staff_subcategory_delete(request,pk):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        qs = get_object_or_404(Subcategory, id=pk).delete()      
        return redirect('staff-subcategory-list')


@login_required
def staff_subcategory_edit(request,pk):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        subcategory = get_object_or_404(Subcategory, id=pk)
        if request.method == 'POST':
                title = request.POST.get('title')
                image_alt = request.POST.get('image-alt')
                new_image = subcategory.image
                if title == "" :

                    messages.error(request, 'یک عنوان برای دسته بندی انتخاب کنید')
                    return redirect(request.path)

                if len(Category.objects.filter(title=title)) > 1 :

                    messages.error(request, 'دسته بندی مورد نظر از قبل موجود است')
                    return redirect(request.path)

                if request.FILES.get('image'):
                
                    myfile = request.FILES['image']
            
                    if str(myfile.content_type).startswith("image"):

                        if myfile.size < 5000000 :    
                            new_image = myfile      
                            
                        else:

                            messages.error(request, 'تصویر انتخاب شده باید کمتر از 5 مگابایت باشد')
                            return redirect(request.path)

                    else:

                        messages.error(request, 'فرمت فایل انتخاب شده برای تصویر پشتیبانی نمیشود')
                        return redirect(request.path)

                subcategory.image = new_image
                subcategory.title = title
                subcategory.image_alt = image_alt
                subcategory.save()
                return redirect('staff-subcategory-list')

        return render(request, 'staff-panel/subcategory-edit.html',{'subcategory':subcategory})

def front_all_subcat_list(request):
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    paginator = Paginator(subcat,6)    
    page = request.GET.get('page')
    paged_subcat = paginator.get_page(page)
    context = {
        'paged_subcat':paged_subcat,
        'cat':cat,
        'subcat':subcat,
    }
    return render(request, 'front/subcategories.html', context)

def front_subcat_list(request,cat_id):
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    selected_cat = get_object_or_404(Category, pk=cat_id)
    selected_subcat = Subcategory.objects.filter(main_cat=selected_cat.id)
    paginator = Paginator(selected_subcat,6)    
    page = request.GET.get('page')
    paged_subcat = paginator.get_page(page)
    context = {
        'paged_subcat':paged_subcat,
        'cat':cat,
        'subcat':subcat,
        'cat_title':selected_cat,
    }
    return render(request, 'front/subcategories.html', context)

def front_subcat_posts(request,subcat_id):
    subcat_posts = get_object_or_404(Subcategory, pk=subcat_id)
    popular_posts = Post.objects.filter(subcategory=subcat_posts).order_by('-likes')[:8]
    most_visited_posts = Post.objects.filter(subcategory=subcat_posts).order_by('-views_count')[:8]
    posts = Post.objects.filter(subcategory=subcat_posts.id,is_published=True)
    paginator = Paginator(posts,8)    
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts':paged_posts,
        'subcat_title': subcat_posts,
        'most_visited_posts':most_visited_posts,
        'popular_posts':popular_posts,
        }
    return render(request, 'front/subcat-posts.html',context)