from rest_framework import serializers
from .models import (
    Room, Occupant
)


class RoomSerializer(serializers.ModelSerializer):
    """
    Map room data to the database.
    """ 
    class Meta:
        model  = Room
        fields = "__all__"


class OccupantSerializer(serializers.ModelSerializer):
    """
    Map occupants data to the occupant database'
    """
    class Meta:
        model  = Occupant
        fields = "__all__"