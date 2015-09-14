'''
View
----
'''

# Third Party Libs
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from userservice.api import serializers


class BaseModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        ''' Overwrite response code to be 200 instead `of` `204` used by Djagno REST

        Arguments:
            request (Request): Djagno REST response class
        '''
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class UserViewSet(BaseModelViewSet):
    ''' User view

    **Example of response:**

    .. code-block:: json

        {
            "items": [
                {
                    "date_joined": "2015-09-02T16:06:11.443066Z",
                    "email": "exampl2e@domain.com",
                    "first_name": "first",
                    "id": 0,
                    "last_login": null,
                    "last_name": "last",
                    "username": "username"
                },
            ],
            "next": null,
            "limit": 25,
            "offset": 0,
            "total": 2,
            "previous": null
        }
    '''

    serializer_class = serializers.UserSerializer
    queryset = User.objects.filter(is_staff=False, is_active=True).all()
