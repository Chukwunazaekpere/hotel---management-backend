from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

import os
import json

from rest_framework.generics import (
    ListAPIView, CreateAPIView, ListCreateAPIView
)

from .models import (
    Room, Occupant, ContactUs
)


from .serializers import (
    RoomSerializer, OccupantSerializer, ContactSerializer
)

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings 




class RoomsListAPIView(ListAPIView):
    """
    This serializer gives a list of available rooms for booking.
    """
    queryset         = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, *args, **kwargs):     
        # Querry the database for only free rooms.   
        get_only_free_rooms = Room.objects.filter(room_status='Free').values()
        
        return Response( get_only_free_rooms )


class CreateOccupantAPIView(CreateAPIView):
    """
    Serialize user details, who would wish to book a room
    """
    queryset         = Occupant.objects.all()
    serializer_class = OccupantSerializer

    def post(self, *args, **kwargs):
        serializer_data = OccupantSerializer(data=self.request.data)
        if serializer_data.is_valid():
            print("\n\t Data valid...")
            paid = False
            kwargs.update({ 'paid': paid })
            serializer_data.save()
            return Response(data='Processed!', status=status.HTTP_201_CREATED)

        return Response(serializer_data.errors, status=status.HTTP_403_FORBIDDEN)

    

class CreatePaymentAPIView(CreateAPIView):
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

class RoomDetailsAPIView(DetailView):
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


class ContactUsAPIView(CreateAPIView):
    serializer_class = ContactSerializer

    def post(self, *args, **kwargs):
        print("\n\t Contacting us...")
        serializer = ContactSerializer(data=self.request.data)

        if serializer.is_valid():
            firstname = serializer.validated_data['firstname']
            lastname  = serializer.validated_data['lastname']
            email     = serializer.validated_data['email']
            serializer.save()

            subject = 'Message Received'
            message = f"Dear {firstname} {lastname} your message has been received,'\
                        ' our frontdesk representative will reply you before 24-hours."
            receipient = email

            with open(os.path.join(os.getcwd(), 'secret_data.json')) as secret_data:
                sender = json.load(secret_data)

            send_mail(
                subject,
                message,
                sender['EMAIL_HOST_USER'],
                [receipient]
            )
            return Response('Message sent.', status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)