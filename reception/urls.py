from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    # ===================== Frontend Routes =========================================
    # Direct all frontend routes to the "HomepageView" at the backend
    path('', views.HomepageView.as_view(), name='homepage'),


    path('occupant-details/', views.HomepageView.as_view(), name='homepage'),

    path('roomlist/', views.HomepageView.as_view(), name='homepage'),

    path('room-reservation/', views.HomepageView.as_view(), name='homepage'),

    path('room-reservation/payment/', views.HomepageView.as_view(), name='homepage'),

    # ===============================================================================
    
    #========================= API Routes ===========================================
    # This url requires a url-argument tagged 'room-type'
    path('roomslist/', views.RoomsList.as_view(), 
                                                    name='roomslist'),

    path('create-occupant/', views.CreateOccupant.as_view(), 
                                                    name='create_occupant'),

    # path('list-assign-occupants/', views.ListAssignOccupants.as_view(), 
    #                                                 name='list_assign_occupants'),

    path('room-details/<slug:room_slug>/', views.RoomDetailsView.as_view(), 
                                                    name='room_details'),

# ===================================Live url====================================
    path('hotel-celetsial.herokuapp.com', views.HomepageView.as_view(), 
                                                    name='homepage'),


]

