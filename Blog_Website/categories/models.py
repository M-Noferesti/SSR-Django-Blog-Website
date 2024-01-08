from django.db import models
from django_jalali.db import models as jmodels


class Category(models.Model):

    title = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='Categories/%Y/%m/%d',blank=True, null=True)
    image_alt = models.CharField(max_length=100,blank=True, null=True)
    posts = models.ManyToManyField('posts.Post',related_name='category_post')
    subcategories = models.ManyToManyField('subcategories.Subcategory',related_name='category_subcategory')
    timestamp = jmodels.jDateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "دسته بندی های اصلی"