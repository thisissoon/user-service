# Standard Libs
import json

# Third Party Libs
import pytest

# First Party Libs
from userservice.api.tests import factories, reverse


@pytest.mark.django_db
def test_resource_return_only_active_users(client):
    factories.UserFactory.create(is_staff=True)
    factories.UserFactory.create(is_active=True)
    factories.UserFactory.create(is_active=False)
    response = client.get(reverse('user'))
    assert json.loads(response.content)['meta']['total_count'] == 1


def test_user_detail_resource_reversible(client):
    assert reverse('user', pk=1) == '/api/v1/user/1/'


def test_user_list_resource_reversible(client):
    assert reverse('user') == '/api/v1/user/'
