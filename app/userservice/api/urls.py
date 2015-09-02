# Third Party Libs
from django.conf.urls import include, patterns
from tastypie import api

# First Party Libs
from userservice.api import resources


v1_api = api.Api(api_name='v1')
v1_api.register(resources.UserResource())


api_urlpatterns = patterns(
    '',
    (r'^api/', include(v1_api.urls))
)
