User endpoint
=============

User endpoint allows us CRUD operation with user accounts.

**URI**: `/api/v1/users/`


Get list of users
-----------------

Endpoint doesn't return non active or staff users.

.. code-block:: bash

    http GET /api/v1/users/


**Response**

.. code-block:: json

    {
        "items": [
            {
                "date_joined": "2015-09-02T16:06:11.443066Z",
                "email": "exampl2e@domain.com",
                "first_name": "first",
                "id": 0,
                "last_login": null,
                "last_name": "last",
                "username": "username"
            },
        ],
        "next": null,
        "limit": 25,
        "offset": 0,
        "total": 5,
        "previous": null
    }

Create new user
---------------

.. code-block:: bash

    http POST /api/v1/users/

.. code-block:: json

    {
        "email": "example@domain.com",
        "first_name": "first",
        "last_name": "last",
        "username": "username",
        "password": "password"
    }


**Response**

.. code-block:: json

    {
        "email": "example@domain.com",
        "first_name": "first",
        "last_name": "last",
        "username": "username",
        "id": "43"
    }


Update existing user
--------------------

Request body is same as for user creation.

.. code-block:: bash

    http PUT /api/v1/users/43

.. code-block:: json

    {
        "email": "example@domain.com",
        "first_name": "first",
        "last_name": "last",
        "username": "username",
        "password": "password"
    }


**Response**

.. code-block:: json

    {
        "email": "example@domain.com",
        "first_name": "first",
        "last_name": "last",
        "username": "username",
        "id": "43"
    }


Delete existing user
--------------------

Delete will remove use from database!

.. code-block:: bash

    http DELETE /api/v1/users/43

