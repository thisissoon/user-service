# Third Party Libs
from django.contrib.auth.models import User
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    pass


class UserSerializer(BaseSerializer):

    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = ('date_joined', 'email', 'first_name', 'id', 'last_login',
                  'last_name', 'username', 'password')

    def create(self, validated_data):
        obj = super(UserSerializer, self).create(validated_data)
        if validated_data.get('password'):
            obj.set_password(validated_data['password'])
            obj.save()
        return obj

    def update(self, instance, validated_data):
        obj = super(UserSerializer, self).update(instance, validated_data)
        if validated_data.get('password'):
            obj.set_password(validated_data['password'])
            obj.save()
        return obj
