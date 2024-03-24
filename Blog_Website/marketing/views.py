from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Marketing,GuestMarketing

@login_required 
def marketing_emails_list(request):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        marketing_emails = Marketing.objects.filter(mailchimp_subscribed=True)
        paginator = Paginator(marketing_emails,10)    
        page = request.GET.get('page')
        paged_marketing_emails = paginator.get_page(page)


        guest_marketing_emails = GuestMarketing.objects.all()
        paginator = Paginator(guest_marketing_emails,10)    
        page = request.GET.get('guest_page')
        paged_guest_marketing_emails = paginator.get_page(page)

        context = {
            'emails' : paged_marketing_emails,
            'guest_emails' : paged_guest_marketing_emails,
            
        }
        return render(request, 'staff-panel/marketing-emails.html',context)

@login_required 
def marketing_emails_delete(request,id):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        email = Marketing.objects.get(id=id).delete()  
        return redirect('marketing-emails-list')

@login_required 
def guest_marketing_emails_delete(request,id):
    if not request.user.profile_user.is_admin:
       return redirect('home')
    else:
        email = GuestMarketing.objects.get(id=id).delete()  
        return redirect('marketing-emails-list')
