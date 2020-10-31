from django.test import (
    TestCase, RequestFactory
)

from ..models import (
    Room, Occupant
)


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.create_room1 = Room.objects.create(
            room_type='Business',
            room_price=4200.00,
            room_number=2,
        )

    def test_room_detail_view(self):
        response = self.client.get('/reception/room-details/Business-2/')
        print("\n\t Response: ", response.content)
        self.assertDictContainsSubset({'room_type':'Business'}, 
                        {"room_type":"Business","room_price":4200.0,
                            "room_number":2,"available":"True"})