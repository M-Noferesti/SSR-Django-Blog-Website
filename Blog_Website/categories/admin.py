from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ( 'title', 'image')
    search_fields = ('title',)
    """     exclude = ('post_count','subcategories_count') """

admin.site.register(Category, CategoryAdmin)