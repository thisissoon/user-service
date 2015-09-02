# Third Party Libs
from django.contrib.auth.models import User
from tastypie.resources import ModelResource


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
