from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    
    # This url requires a url-argument tagged 'room-type'
    path('roomslist/<str:room_type>/', views.ListRooms.as_view(), 
                                                    name='roomslist'),

    path('create-occupant/', views.CreateOccupant.as_view(), 
                                                    name='create_occupant'),

    # path('list-assign-occupants/', views.ListAssignOccupants.as_view(), 
    #                                                 name='list_assign_occupants'),

    path('room-details/<slug:room_slug>/', views.RoomDetailsView.as_view(), 
                                                    name='room_details'),

]

