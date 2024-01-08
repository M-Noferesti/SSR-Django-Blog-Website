from django.urls import path
from . import views

urlpatterns = [

    path('staff_panel/category_list', views.staff_category_list, name='staff-category-list'),
    path('staff_panel/category_add', views.staff_category_add, name='staff-category-add'),
    path('staff_panel/category_delete/<int:pk>/', views.staff_category_delete, name='staff-category-delete'),
    path('staff_panel/category_edit/<int:pk>/', views.staff_category_edit, name='staff-category-edit'),
    path('categories', views.user_category_list, name='user-category-list'),

]