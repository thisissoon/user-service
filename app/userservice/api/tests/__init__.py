# Third Party Libs
from django.core import urlresolvers


def reverse(resource, pk=None, version='v1'):
    endpoint = {'resource_name': resource, 'api_name': version}
    if pk is not None:
        endpoint.update({'pk': pk})
        return urlresolvers.reverse('api_dispatch_detail', kwargs=endpoint)
    return urlresolvers.reverse('api_dispatch_list', kwargs=endpoint)
