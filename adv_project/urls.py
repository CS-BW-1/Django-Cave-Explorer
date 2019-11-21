from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from api.api import PlayerViewSet, RoomViewSet
from rest_framework import routers

from rest_framework.authtoken import views

import sys

# sys.path.insert(1, '/path/to/application/')

router = routers.DefaultRouter()
router.register('players', PlayerViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth', views.obtain_auth_token),

]
