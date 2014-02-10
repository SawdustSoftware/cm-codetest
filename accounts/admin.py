""" Configuration for UserData in the Admin panel """
from django.contrib import admin
from django.conf import settings
from models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    """Display Custom User model in the admin

    Note: we use the Twitter username for the username
    """
    fields = ('username', 'photo', 'first_name', 'last_name', 'date_joined',)
    list_display = ('username', 'display_avatar', 'first_name', 'last_name', 'date_joined',)
    list_filter = ('username', 'first_name', 'last_name', 'date_joined',)

    def display_avatar(self, instance):
        """Return html for user photo so their profile image is displayed """
        return '<img src="%s"/>' % (settings.MEDIA_URL + instance.photo.__unicode__())

    display_avatar.short_description = 'avatar'
    display_avatar.allow_tags = True

admin.site.register(CustomUser, CustomUserAdmin)



