from django import forms

from .models import Tweet


class TweetsForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('message',)

    def __init__(self, user, *args, **kwargs):
        """Store user for later use and add error message"""
        super(TweetsForm, self).__init__(*args, **kwargs)
        self.user = user

        # add custom error messages
        self.fields['message'].error_messages = {'required': 'We need a message in order to tweet!'}

    def save(self, commit=True):
        """
        TODO: Add user to created_by field, parse tweet to find category/product and post twitter status

        But remember, only posts to twitter if a category is found in the tweet
        """


        raise NotImplementedError("Need to implement save method on TweetsForm")