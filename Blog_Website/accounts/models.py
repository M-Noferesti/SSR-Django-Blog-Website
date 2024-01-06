from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile_user")
    avatar = models.ImageField(upload_to='Avatars/%Y/%m/%d',blank=True, null=True)
    bio = models.CharField(max_length=400,blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    writed_posts = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    favorite_posts = models.ManyToManyField('posts.Post',blank=True,related_name='favorite_posts')
    read_later_posts = models.ManyToManyField('posts.Post',blank=True,related_name='read_later_posts')
    last_activity = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "حساب ها"   
    

def create_account(sender, instance, created, *args, **kwrags):
    if created:
       account = Account.objects.create(user=instance,is_admin=instance.is_superuser)
post_save.connect(create_account,sender=User)


def edit_account(sender, instance, *args, **kwrags):
    account = Account.objects.get(user__id=instance.id)
    account.is_admin=instance.is_superuser
    account.save()
post_save.connect(edit_account,sender=User)

       