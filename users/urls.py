from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),

    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('confirm-email/<str:token>/', views.confirmEmail, name='account_confirm_email'),
]

