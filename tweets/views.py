import twitter
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from braces.views import LoginRequiredMixin

from forms import TweetsForm
from models import get_default_category

class Index(LoginRequiredMixin, View):
    """ View -- Handles all tweet submissions """
    form_class = TweetsForm

    def post(self, request, *args, **kwargs):
        """ Verify tweet submission is valid, handles errors and posts to Twitter if appropriate"""
        form = self.form_class(data=request.POST, user=request.user)

        if form.is_valid():
            instance = form.save()

            # Deal with posting twitter status
            posted_status = False
            if instance.category != get_default_category():
                # Create tweeted message and post status
                tweeted_message = "RT:<%s>%s#Custom#%s" % (instance.created_by.username, instance.message, instance.category)
                api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                                  access_token_key=settings.TWITTER_USER_OAUTH_TOKEN, access_token_secret=settings.TWITTER_USER_OAUTH_TOKEN_SECRET)
                api.PostUpdate(status=tweeted_message)

                # Save time published and update postedStatus
                instance.published_on = timezone.now()
                instance.save()
                posteds_status = True

            return render(request, 'tweets/index.html', {'form': self.form_class(user=request.user), 'success': True, 'posted_status': posted_status})
        return render(request, 'tweets/index.html', {'form': form})

    def get(self, request, *args, **kwargs):
        """ Display the Tweet form """
        return render(request, 'tweets/index.html', {'form': self.form_class(user=request.user)})


