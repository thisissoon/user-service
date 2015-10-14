# Third Party Libs
import mock
from allauth.account.models import EmailConfirmation
from django.test import TestCase


class UserSignUpTestCase(TestCase):

    @mock.patch('userservice.app.sdk.VerificationEmail')
    def test_verification_email_is_send(self, verification):
        resp = self.client.post(
            '/api/v1/registration/',
            {
                'username': 'johndoe',
                'email': 'john@doe.com',
                'password1': 'johndoe',
                'password2': 'johndoe'
            },
            follow=True
        )
        assert 201 == resp.status_code
        verification.assert_called_once_with(EmailConfirmation.objects.first())
