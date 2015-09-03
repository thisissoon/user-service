# Third Party Libs
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(user_logged_in)
def generate_token(sender, **kwargs):
    Token.objects.get_or_create(user=kwargs['user'])
