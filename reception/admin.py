from django.contrib import admin

from .models import (
    Room, Occupant
)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display  = ['room_type', 'room_number', 'room_price', 'room_status']
    list_filter   = [ 'room_status']
    list_editable = ['room_status']
    search_fields = ['room_type']


@admin.register(Occupant)
class OccupantAdmin(admin.ModelAdmin):
    list_display  = ['firstname', 'lastname', 'email', 'duration']
    list_filter   = ['duration']
    list_editable = ['duration']

