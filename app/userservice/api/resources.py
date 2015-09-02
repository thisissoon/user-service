# Third Party Libs
from django.contrib.auth.models import User
from tastypie.resources import ModelResource


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.filter(is_staff=False, is_active=True).all()
        resource_name = 'user'
        allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
        excludes = ('password', 'is_active', 'is_staff', 'is_superuser', )
