'''
Pagination module
-----------------

Defines pagination response payload.
'''

# Third Party Libs
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class Pagination(LimitOffsetPagination):

    default_limit = 25
    max_limit = 50

    def get_paginated_response(self, data):
        ''' Example of paginated response:

        .. code-block:: json

            {
                "items": [],
                "next": null,
                "limit": 25,
                "offset": 0,
                "total": 2,
                "previous": null
            }
        '''
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total': self.count,
            'items': data,
            'limit': self.limit,
            'offset': self.offset,
        })
