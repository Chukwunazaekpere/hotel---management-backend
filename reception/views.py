from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


from rest_framework.generics import (
    ListAPIView, CreateAPIView, ListCreateAPIView
)

from .models import (
    Room, Occupant
)

from django.views.generic import (
    DetailView
)

from .serializers import (
    RoomSerializer, OccupantSerializer
)

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings 


class ListRooms(ListAPIView):
    """
    This serializer gives a list of available rooms for booking.
    """
    queryset         = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, *args, **kwargs):
        room_type = kwargs['room_type'].title()
        print("\n\troom_type: ",room_type)
        
        get_rooms_by_room_type = Room.objects.filter(room_type=room_type).values()

        # get_only_free_rooms = Room.objects.filter(room_status='Free').values()
        
        return Response( get_rooms_by_room_type )


class CreateOccupant(CreateAPIView):
    """
    Serialize user details, who would wish to book a room
    """
    queryset         = Occupant.objects.all()
    serializer_class = OccupantSerializer
    

class CreatePayment(CreateAPIView):
    queryset = Occupant.objects.all()
    serializer_class = OccupantSerializer

    # This view creates a new occupant by accepting their details,
    # sending mails and as well, listing occupants in various rooms
    def post(self, request, *args, **kwargs):
        serializer = OccupantSerializer(data=request.data)

        if serializer.is_valid():
            # Get appl
            ("\n\t Now in post serializer...")
            print("\n\t Data: ", serializer.data)

            email     = serializer.data["email"]
            firstname = serializer.data["firstname"]
            lastname  = serializer.data["lastname"]

            new_occupant = Occupant()
            new_occupant.duration = serializer.data['duration']
            new_occupant.phone = serializer.data['phone']

            subject = "Booking details"
            html_message = render_to_string(
                "reception/templates/emailVerficationToPaymentPage.html",
                {
                    "firstname": firstname,
                    "lastname": lastname,
                    "subject": subject
                }
            )

            # If receipients browser isn't html capable, use "plain_message".
            plain_message = strip_tags(html_message) 
            sender = settings.get_secret_data('EMAIL_HOST_USER')

            # Now send mail to receipient
            send_mail(
                subject,
                plain_message,
                sender,
                [email],
                fail_silently=True,
                html_message=html_message
            )
            return Response(new_occupant, status=status.HTTP_202_ACCEPTED)

class RoomDetailsView(DetailView):
    """
    Prepare data for an end-point to receive the details of a room.
    """
    model = Room

    def get(self, request, *args, **kwargs):
        # get the slug of the requested room whose details are needed.
        slug_of_requested_room = kwargs['room_slug']  
        room_details = get_object_or_404(Room, slug=slug_of_requested_room)

        data = {
            'room_type': room_details.room_type,
            'room_price': room_details.room_price,
            'room_number': room_details.room_number,
            'available': room_details.room_status
        }

        response = Response(data, status=status.HTTP_200_OK,
                            content_type='application/json')

        # the reason for the lines below, is so as to avoid rendering errors; 
        # since we're not rendering directly to a template.
        response.accepted_renderer   = JSONRenderer() 
        response.accepted_media_type = 'application/json'
        response.renderer_context    = {}
        return response


