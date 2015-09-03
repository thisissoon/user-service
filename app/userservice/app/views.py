# Standard Libs
import json

# Third Party Libs
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialApp
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def detail(request):
    dict_providers = {}
    media = {}
    for provider in SocialApp.objects.all():
        provider = providers.registry.by_id(provider.provider)
        extra_params = {'next': request.GET.get('next')} if request.GET.get('next') else {}
        if provider.name.lower() == 'facebook':
            key = '{}-js'.format(provider.name.lower())
            dict_providers[key] = provider.get_login_url(
                request, method='js_sdk', **extra_params
            )
            media[key] = provider.media_js(request)
        dict_providers[provider.name.lower()] = provider.get_login_url(
            request, **extra_params
        )

    response_data = {
        'logout': reverse('account_logout'),
        'providers': dict_providers,
        'media': media
    }

    return HttpResponse(
        json.dumps(response_data),
        content_type='application/json'
    )


class TokenView(APIView):

    authentication_classes = (authentication.SessionAuthentication,
                              authentication.BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        response_data = {
            'token': Token.objects.get_or_create(user=request.user)[0].key,
        }

        return Response(response_data)
