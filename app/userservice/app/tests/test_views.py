# Standard Libs
import httplib
import json

# Third Party Libs
import pytest
from allauth.socialaccount.models import SocialApp
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_auth_endpoint(client):
    socialapp = SocialApp(
        provider='twitter',
        name='twitter 12',
        client_id='fasdfds',
        secret='fadsf5dgs',
    )
    socialapp.save()

    response = client.get(reverse('oauth'))
    data = json.loads(response.content)

    assert data['providers']['twitter'] == '/accounts/twitter/login/'


@pytest.mark.django_db
def should_be_logged_in_to_get_token(client):
    response = client.get(reverse('token'))
    assert response.status_code == httplib.FORBIDDEN


@pytest.mark.django_db
def should_be_get_user_token():
    user = get_user_model().objects.create_user('test', 'test@test.co', 'test')
    client = APIClient()
    client.login(username='test', password='test')
    response = client.get(reverse('token'))

    assert response.status_code == httplib.OK
    assert Token.objects.get(user=user).key == response.data['token']
