# Third Party Libs
from django.contrib.auth.models import User
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    pass


class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        fields = ('date_joined', 'email', 'first_name', 'id', 'last_login',
                  'last_name', 'username', )
