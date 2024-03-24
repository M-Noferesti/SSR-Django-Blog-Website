from django.urls import path
from . import views
urlpatterns = [
    path('staff_panel/marketing_emails_list/', views.marketing_emails_list, name='marketing-emails-list'),
    path('staff_panel/marketing_emails_list/delete/<int:id>/', views.marketing_emails_delete, name='marketing-emails-delete'),
    path('staff_panel/marketing_emails_list/delete_guest/<int:id>/', views.guest_marketing_emails_delete, name='guest-marketing-emails-delete'),
 ]