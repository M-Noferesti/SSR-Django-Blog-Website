from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password-again']
        
        if password == password_again:
            if User.objects.filter(username=username).exists():
                messages.error(request,'این نام کاربری از قبل وجود دارد')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'این ایمیل از قبل وجود دارد')
                    return redirect('register')
                else:                
                    user = User.objects.create_user(username=username, first_name=first_name,
                    last_name= last_name,email=email, password=password)
                    user.save()
                    messages.success(request, 'ثبت نام شما با موفقیت انجام شد، حالا می توانید وارد حساب خود شوید')
                    return redirect('login')
        else:
            messages.error(request,'رمز عبور تکرار شده همسان نیست')
            return redirect('register')
    else:
        return render(request, 'front/accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        previous_page = request.POST['previous-page']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.profile_user.is_admin or user.profile_user.is_writer:
                if previous_page and previous_page != "http://127.0.0.1:8000/login" :
                    messages.success(request, 'ورود شما با موفقیت انجام شد')
                    return redirect(previous_page)
                    
                else:

                    return redirect('staff-panel')
            else:
                if previous_page and previous_page != "http://127.0.0.1:8000/login" :
                    
                    messages.success(request, 'ورود شما با موفقیت انجام شد')
                    return redirect(previous_page)
                else:
                    return redirect('user-panel')
                    
        else:
            
            messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد')
            return redirect('login')
    else:
        return render(request, 'front/accounts/login.html')

def logout(request):
        auth.logout(request)
        return redirect('home')




