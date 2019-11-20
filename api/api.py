from adventure.models import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import serializers, viewsets


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'currentRoom')

    # def create(self, validated_data):
    #     import pdb
    #     # pdb.set_trace()  # debugger
    #     user = self.context['request'].user

    #     print(user.user_id)
    #     player = Player.objects.create(user=user, **validated_data)
    #     return player


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'n_to',
                  's_to', 'e_to', 'w_to')

    def create_room(self, validated_data):
        import pdb
        # pdb.set_trace()  # debugger

        room = Room.objects.create_room(**validated_data)
        return room


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
