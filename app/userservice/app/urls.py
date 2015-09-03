# Third Party Libs
from django.conf.urls import patterns, url

# First Party Libs
from userservice.app import views


urlpatterns = patterns(
    '',
    url(r'^accounts/$', views.detail, name='oauth'),
    url(r'^token/$', views.TokenView.as_view(), name='token'),
)
