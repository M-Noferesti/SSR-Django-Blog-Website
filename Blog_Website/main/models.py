from django.db import models


class SocialPages(models.Model):
    instagram = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()
    
    def __str__(self):
        return 'social pages information'
    class Meta:
        verbose_name_plural = "صفحات اجتماعی"   