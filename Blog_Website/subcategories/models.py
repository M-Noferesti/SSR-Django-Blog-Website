from __future__ import unicode_literals
from django.db.models.signals import post_save, post_delete
from django.db import models
from django_jalali.db import models as jmodels
from categories.models import Category

class Subcategory(models.Model):

    title = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='Subcategories/%Y/%m/%d',blank=True, null=True)
    image_alt = models.CharField(max_length=100,blank=True, null=True)
    main_cat = models.ForeignKey(Category,on_delete=models.CASCADE)    
    posts = models.ManyToManyField('posts.Post',related_name='subcategory_post')
    timestamp = jmodels.jDateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "دسته بندی های فرعی"   

def add_subcategory_to_category(sender, instance, *args, **kwrags):

        qs = Category.objects.get(id=instance.main_cat.id)
        if instance not in qs.subcategories.all():
            qs.subcategories.add(instance)
            qs.save()
post_save.connect(add_subcategory_to_category,sender=Subcategory)
    
def remove_subcategory_to_category(sender, instance, *args, **kwrags):
        qs = Category.objects.get(id=instance.main_cat.id)
        if instance in qs.subcategories.all():
            qs.subcategories.remove(instance)
            qs.save()
post_delete.connect(remove_subcategory_to_category,sender=Subcategory)