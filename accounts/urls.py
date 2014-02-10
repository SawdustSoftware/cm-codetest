from django.conf.urls import patterns, url
from views import Logout

urlpatterns = patterns('',
    url(r'^$', Logout.as_view(), name='logout'),
)