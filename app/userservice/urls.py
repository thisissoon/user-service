# Third Party Libs
from django.conf.urls import include, url
from django.contrib import admin

# First Party Libs
from userservice.api.urls import api_urlpatterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
] + api_urlpatterns
