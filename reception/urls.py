from django.urls import path, include
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
    # ===================================Live url====================================
    path('hotel-celetsial.herokuapp.com', views.HomepageView.as_view(), 
                                                    name='homepage'),


]

