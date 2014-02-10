""" Customization to the twitter sign-in pipeline from social_auth """
from urllib2 import urlopen
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from social_auth.backends.twitter import TwitterBackend

def get_avatar_url(request, backend, response, *args, **kwargs):
    """ Grabs avatar from twitter and stores in user model

    If photo already exists, no new photo is stored"""

    # Check to make sure user doesn't already have a photo
    user = kwargs['user']
    if user.photo:
        return

    # Otherwise add photo
    if isinstance(backend, TwitterBackend):
        avatar_url = response.get('profile_image_url', '')
        avatar = urlopen(avatar_url)
        user.photo.save(slugify(user.username + " social") + '.jpg',
                        ContentFile(avatar.read()))
        user.save()

