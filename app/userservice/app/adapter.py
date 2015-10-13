from allauth.account.adapter import DefaultAccountAdapter
from userservice.app.sdk import VerificationEmail


class MyAccountAdapter(DefaultAccountAdapter):
    """ Overwrite sending verification email
    """

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        """ Send confirmation email that user is registered

        Arguments
        ---------
            request: Django request
            emailconfirmation (allauth.account.models.EmailConfirmation):
                has reference to an user
            signup (boolean)
        """
        VerificationEmail(emailconfirmation).send()
