from rest_framework import routers
from userservice.api import views

v1 = routers.DefaultRouter()
v1.register(r'users', views.UserViewSet)
