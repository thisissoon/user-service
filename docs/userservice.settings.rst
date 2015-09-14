Settings
========

Standard Django settings modules.


Submodules
----------

userservice.settings.base module
--------------------------------

This module is based and should not be used directly. It's intended to load
middlewares, installed apps, configure another module like Django REST framework, etc.


userservice.settings.dev module
-------------------------------

Used for local testing. Module shouldn't use any external services like storages or
shared cached.


userservice.settings.qa module
------------------------------

Used for QA the module is most similar to production environment.


userservice.settings.test module
--------------------------------

Used for testing - no cache, simple password hashing, temporary file as media
root, ...
