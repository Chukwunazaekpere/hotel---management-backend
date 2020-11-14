from django.test import TestCase
from ..models import (
    Room, Occupant
)

class TestModels(TestCase):
    def setUp(self):
        self.create_room1 = Room.objects.create(
            room_type='Executive',
            room_price=40000.00,
            room_number=3,
            available=False
        )

    def test_save_method_of_room_model(self):
        """
        Assert that a new room has been created
        """
        number_of_rooms = len(Room.objects.all())
        # print(Room.objects.get(room_number=3).available)
        self.assertEquals(number_of_rooms, 1)


    def test_absolute_url_method_of_room_model(self):
        """
        Assert that the 'get_absolute_url' method returns the details of a
        room.
        """
        room_detail = self.create_room1.get_absolute_url()
        self.assertEquals(room_detail, '/reception/room-details/Executive-3/')

