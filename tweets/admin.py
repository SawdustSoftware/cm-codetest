""" Configurations to Admin Panel for TweetData"""

from django.contrib import admin
from models import Tweet
from django.core.urlresolvers import reverse


class TweetsAdmin(admin.ModelAdmin):
    """Displays Tweet Data in admin"""
    list_display = ('twitter_username', 'message', 'created', 'category', 'product', 'published_on')
    list_display_links = ('twitter_username', )

    def twitter_username(self, instance):
        """Return link to edit User page"""
        url = reverse('admin:accounts_customuser_change', args=(instance.created_by.id,))
        return '<a href="%s">%s</a>' % (url, instance.created_by.username)

    twitter_username.short_description = 'Twitter Username'
    twitter_username.allow_tags = True


admin.site.register(Tweet, TweetsAdmin)