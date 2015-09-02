# Third Party Libs
from django.contrib.auth.models import User
from rest_framework import viewsets
from userservice.api import serializers
from rest_framework.response import Response
from rest_framework import status


class BaseModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class UserViewSet(BaseModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = User.objects.filter(is_staff=False, is_active=True).all()