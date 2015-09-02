# Standard Libs
import json

# Third Party Libs
import httplib
import pytest
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

# First Party Libs
from userservice.api.tests import factories


def test_user_detail_resource_is_reversible(client):
    assert reverse('user-detail', args=(1, )) == '/api/v1/users/1/'


def test_user_list_resource_is_reversible(client):
    assert reverse('user-list') == '/api/v1/users/'


@pytest.mark.django_db
def should_return_only_active_users(client):
    factories.UserFactory.create(is_staff=True)
    factories.UserFactory.create(is_active=True)
    factories.UserFactory.create(is_active=False)
    response = client.get(reverse('user-list'))
    assert json.loads(response.content)['total'] == 1


@pytest.mark.django_db
def should_creste_new_user(client):
    payload = {
        'email': 'example@domain.com',
        'first_name': 'first',
        'last_name': 'last',
        'username': 'username',
        'password': 'password',
    }
    response = client.post(
        reverse('user-list'),
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert httplib.CREATED == response.status_code, response.content
    assert '' != response.content

    created_user = get_user_model().objects.first()
    assert created_user.email == 'example@domain.com'
    assert client.login(username='username', password='password')


@pytest.mark.django_db
def should_update_user(client):
    user = factories.UserFactory.create(is_active=True)
    payload = {
        'username': 'username',
        'email': 'example@domain.com',
    }
    response = client.put(
        reverse('user-detail', args=(user.pk, )),
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert httplib.OK == response.status_code, response.content
    assert '' != response.content

    created_user = get_user_model().objects.get(pk=user.pk)
    assert 'example@domain.com' == created_user.email
    assert '' != response.content


@pytest.mark.django_db
def should_change_user_password(client):
    user = factories.UserFactory.create(is_active=True)
    payload = {
        'username': 'username',
        'password': 'password',
    }
    response = client.put(
        reverse('user-detail', args=(user.pk, )),
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert httplib.OK == response.status_code, response.content
    assert '' != response.content
    assert client.login(username='username', password='password')


@pytest.mark.django_db
def should_return_404_for_updating_non_existing_user(client):
    response = client.put(
        reverse('user-detail', args=(0, )),
        data=json.dumps({'email': 'example@domain.com'}),
        content_type='application/json'
    )
    assert httplib.NOT_FOUND == response.status_code


@pytest.mark.django_db
def should_delete_user(client):
    user = factories.UserFactory.create(is_active=True)

    response = client.delete(
        reverse('user-detail', args=(user.pk, ))
    )
    assert httplib.OK == response.status_code
    assert '' == response.content

    deleted_user = get_user_model().objects.filter(pk=user.pk).first()
    assert deleted_user is None


@pytest.mark.django_db
def should_return_404_for_deletion_non_existing_user(client):
    response = client.delete(reverse('user-detail', args=(0, )))
    assert httplib.NOT_FOUND == response.status_code


@pytest.mark.django_db
def test_detail_field(client):
    factories.UserFactory.create(is_staff=True)
    user = factories.UserFactory.create(is_active=True)
    factories.UserFactory.create(is_active=False)

    expected = [
        'date_joined', 'email', 'first_name', 'id', 'last_login', 'last_name',
        'username',
    ]
    response = client.get(reverse('user-detail', args=(user.pk, )))
    assert set(expected) == set(json.loads(response.content).keys())


@pytest.mark.django_db
def test_list_field(client):
    factories.UserFactory.create(is_active=True)

    expected = [
        'date_joined', 'email', 'first_name', 'id', 'last_login', 'last_name',
        'username',
    ]
    response = client.get(reverse('user-list'))
    assert set(expected) == set(json.loads(response.content)['items'][0].keys())
