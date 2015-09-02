# Third Party Libs
from django.contrib.auth.models import User
from django.http import HttpResponse
from tastypie import http
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.exceptions import NotFound
from tastypie.resources import ModelResource


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.filter(is_staff=False, is_active=True).all()
        resource_name = 'user'

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']

        excludes = ('password', 'is_active', 'is_staff', 'is_superuser', )

        authorization = Authorization()

        always_return_data = True

    def delete_detail(self, request, **kwargs):
        """
        Destroys a single resource/object.
        Calls ``obj_delete``.
        If the resource is deleted, return ``response`` (200 OK).
        If the resource did not exist, return ``Http404`` (404 Not Found).
        """
        # Manually construct the bundle here, since we don't want to try to
        # delete an empty instance.
        bundle = Bundle(request=request)

        try:
            self.obj_delete(bundle=bundle, **self.remove_api_resource_names(kwargs))
            return HttpResponse()
        except NotFound:
            return http.HttpNotFound()
