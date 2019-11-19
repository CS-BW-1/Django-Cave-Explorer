from django.conf.urls import url
from django.urls import path, include
from . import api
from rest_framework import routers
# importing from the file


urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),

]
