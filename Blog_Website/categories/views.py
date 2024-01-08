from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Category
from subcategories.models import Subcategory
from django.http import HttpResponse



@login_required
def staff_category_list(request):
    if not request.user.profile_user.is_writer and not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        category = Category.objects.all()
        paginator = Paginator(category,10)    
        page = request.GET.get('page')
        paged_category = paginator.get_page(page)

        context = {
            'categories':paged_category,
        }

        return render(request, 'staff-panel/category-list.html',context)


@login_required
def staff_category_add(request):
    if not request.user.profile_user.is_writer and not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            image_alt = request.POST.get('image-alt')

            if title == "" :

                messages.error(request, 'یک نام برای دسته بندی انتخاب کنید')
                return redirect('staff-category-add')

            if len(Category.objects.filter(title=title)) != 0 :

                messages.error(request, 'دسته بندی مورد نظر از قبل موجود است')
                return redirect('staff-category-add')

            try:
            
                myfile = request.FILES['image']
        
                if str(myfile.content_type).startswith("image"):

                    if myfile.size < 5000000 :    
                            
                        category_add = Category.objects.create(title=title,image=myfile,image_alt=image_alt)
                        if request.POST.get('save_and_return'):
                            return redirect('staff-category-list')
                        elif request.POST.get('save_and_another'):
                            return redirect('staff-category-add')

                    else:

                        messages.error(request, 'تصویر انتخاب شده باید کمتر از 5 مگابایت باشد')
                        return redirect('staff-category-add')

                else:

                    messages.error(request, 'فرمت فایل انتخاب شده برای تصویر پشتیبانی نمیشود')
                    return redirect('staff-category-add')

            except:

                messages.error(request, 'تصویری را برای دسته بندی انتخاب کنید')
                return redirect('staff-category-add')

        return render(request, 'staff-panel/category-add.html')


@login_required
def staff_category_delete(request,pk):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        qs = get_object_or_404(Category, id=pk).delete()      
        return redirect('staff-category-list')


@login_required
def staff_category_edit(request,pk):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        category = get_object_or_404(Category, id=pk)
        if request.method == 'POST':
                title = request.POST.get('title')
                image_alt = request.POST.get('image-alt')
                new_image = category.image
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

                category.image = new_image
                category.title = title
                category.image_alt = image_alt
                category.save()
                return redirect('staff-category-list')

        return render(request, 'staff-panel/category-edit.html',{'category':category})

def user_category_list(request):

    cat = Category.objects.all()
    paginator = Paginator(cat,8)    
    page = request.GET.get('page')
    paged_cat = paginator.get_page(page)

    context = {
        'paged_cat':paged_cat,
        'cat':cat,
    }
    return render(request, 'front/categories.html',context)


