from django.urls import path
from . import views

urlpatterns = [

    path('staff_panel/subcategory_list', views.staff_subcategory_list, name='staff-subcategory-list'),
    path('staff_panel/subcategory_add', views.staff_subcategory_add, name='staff-subcategory-add'),
    path('staff_panel/subcategory_delete/<int:pk>/', views.staff_subcategory_delete, name='staff-subcategory-delete'),
    path('staff_panel/subcategory_edit/<int:pk>/', views.staff_subcategory_edit, name='staff-subcategory-edit'),
    path('subcategories', views.front_all_subcat_list, name='front_all_subcat_list'),
    path('categories/subcategories/<int:cat_id>', views.front_subcat_list, name='front_subcat_list'),
    path('categories/<int:subcat_id>', views.front_subcat_posts, name='subcat_posts'),

]

