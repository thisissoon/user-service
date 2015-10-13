# Third Party Libs
from django.conf.urls import include, url
from django.contrib import admin

from userservice.app.views import FacebookLogin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/facebook/$', FacebookLogin.as_view(), name='fb_login')
]
