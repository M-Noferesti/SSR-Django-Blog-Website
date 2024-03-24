from django.contrib import admin
from .models import Marketing, GuestMarketing

class MarketingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscribed', 'update']
    readonly_fields = ['mailchimp_msg', 'mailchimp_subscribed', 'timestamp', 'update']
    class Meta:
        model = Marketing
        fields = [ 
            'user',
            'subscribed',
            'mailchimp_msg',
            'mailchimp_subscribed',
            'timestamp',
            'update'
        ]

admin.site.register(Marketing, MarketingAdmin)
admin.site.register(GuestMarketing)