""" All models needed for account registration """
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """ Model -- Stores information on users

    This model extends default Django User and adds photo field
    """
    photo = models.ImageField(upload_to='profiles/', null=True)