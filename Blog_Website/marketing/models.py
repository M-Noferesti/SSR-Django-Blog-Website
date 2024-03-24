from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from .utils import Mailchimp

class Marketing(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    subscribed = models.BooleanField(default=True)
    mailchimp_subscribed = models.BooleanField(null=True) 
    mailchimp_msg = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    class Meta:
        verbose_name_plural = "ایمیل های بازاریابی کاربران"   



class GuestMarketing(models.Model):
    guest_email = models.EmailField(unique=True)

    def __str__(self):
        return self.guest_email
    class Meta:
        verbose_name_plural = "ایمیل های بازاریابی مهمانان"   

def subscribe_user(sender, instance, created, *args, **kwrags):
    if created:
        status_code, response_data = Mailchimp().subscribe(instance.user.email)
post_save.connect(subscribe_user,sender=Marketing)


def unsubscribe_user(sender, instance, *args, **kwrags):
    status_code, response_data = Mailchimp().unsubscribe(instance.user.email)
pre_delete.connect(unsubscribe_user,sender=Marketing)


def marketing_update_receiver(sender, instance, *args, **kwrags):
    if instance.subscribed != instance.mailchimp_subscribed:
        if instance.subscribed:
            status_code, response_data = Mailchimp().subscribe(instance.user.email)
        else:
            status_code, response_data = Mailchimp().unsubscribe(instance.user.email)
        if response_data['status'] == 'subscribed':
            instance.subscribed = True
            instance.mailchimp_subscribed = True
            instance.mailchimp_msg = response_data
        else:
            instance.subscribed = False
            instance.mailchimp_subscribed = False
            instance.mailchimp_msg = response_data
pre_save.connect(marketing_update_receiver,sender=Marketing)     



def make_marketing_receiver(sender, instance, created, *args, **kwrags):
    if created:
        if instance.is_staff == False and instance.is_superuser == False:
            Marketing.objects.get_or_create(user=instance)
post_save.connect(make_marketing_receiver,sender=settings.AUTH_USER_MODEL)


""" def unsubscribe_staff_receiver(sender, instance, *args, **kwrags):
    if instance.is_staff == True or instance.is_superuser == True:
        status_code, response_data = Mailchimp().unsubscribe(instance.email)
    elif instance.is_staff == False and instance.is_superuser == False:
        status_code, response_data = Mailchimp().subscribe(instance.email)
post_save.connect(unsubscribe_staff_receiver,sender=settings.AUTH_USER_MODEL) """

def subscribe_guest(sender, instance, *args, **kwrags):

    status_code, response_data = Mailchimp().subscribe(instance.guest_email)
post_save.connect(subscribe_guest,sender=GuestMarketing)


def unsubscribe_guest(sender, instance, *args, **kwrags):
    status_code, response_data = Mailchimp().unsubscribe(instance.guest_email)
pre_delete.connect(unsubscribe_guest,sender=GuestMarketing)