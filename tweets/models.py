from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class DefaultManager(models.Manager):
    """
    Provides a 'default' method to grab the default instance
    for a given model
    """

    def default(self):
        """ 
        returns object instance with a name of 'Unknown'
        """
        return self.get(name='Unknown')


class Category(TimeStampedModel):
    """
    Categories of products
    """
    name = models.CharField(_(u'Category Name'), max_length=255)

    objects = DefaultManager()

    def __unicode__(self):
        return self.name


class Product(TimeStampedModel):
    """ 
    Product information
    """
    name = models.CharField(_(u'Product Name'), max_length=255)
    category = models.ForeignKey(Category)

    objects = DefaultManager()

    def __unicode__(self):
        return self.name


def get_default_product():
    """
    Returns the default 'Unknown' product
    """
    return Product.objects.get_or_create(name='Unknown', category=get_default_category())


def get_default_category():
    """
    Returns the default 'Unknown' category
    """
    return Category.objects.get_or_create(name='Unknown')[0]


def validate_length(string):
    """
    Validates that string is less than 110 chars

    Acts as validator for Tweets
    """
    if len(string) > 110:
        raise ValidationError('Tweet must be less than 110 characters')


class Tweet(TimeStampedModel):
    """ 
    Tweet Information
    """
    message = models.TextField(_(u'Message to tweet'), max_length=110, blank=False, validators=[validate_length])
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
    category = models.ForeignKey(Category, default=get_default_category)
    product = models.ForeignKey(Product, default=get_default_product)
    published_on = models.DateTimeField(null=True)


