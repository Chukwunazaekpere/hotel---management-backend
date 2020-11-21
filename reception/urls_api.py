from django.urls import path, include
from . import views_api

app_name = 'room'

urlpatterns = [
    #========================= API Routes ===========================================
    path('api/roomslist/', views_api.RoomsListAPIView.as_view(), 
                                                    name='roomslist'),

    path('api/create-occupant/', views_api.CreateOccupantAPIView.as_view(), 
                                                    name='create_occupant'),

    path('api/room-details/<slug:room_slug>/', views_api.RoomDetailsAPIView.as_view(), 
                                                    name='room_details'),

    path('api/contact-us/', views_api.ContactUsAPIView.as_view(), 
                                                    name='contact_us'),

]

