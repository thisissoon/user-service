# Third Party Libs
from django.conf.urls import include, url
from django.contrib import admin

# First Party Libs
from userservice.api.routers import v1


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(v1.urls)),
    url(r'^app/', include('userservice.app.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
