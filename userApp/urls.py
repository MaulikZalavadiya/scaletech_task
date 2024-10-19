from django.urls import include, path

from rest_framework import routers

# from realtorx.agencies import api
from .views import *

router = routers.SimpleRouter()
router.register(r'roles', RoleViewSet, basename='userroles')
router.register(r'users', UserViewSet,basename='users')


app_name = 'userApp'
urlpatterns = [

    path('sigup', signup_API),
    path('login', LoginAPI),
    path('logout', LogoutAPI)
]+router.urls
