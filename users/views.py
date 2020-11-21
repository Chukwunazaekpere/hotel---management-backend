from django.shortcuts import render
from .serializers import RegisterSerializer

from rest_framework.generics import (
    CreateAPIView
)

from .models import Users

    
def confirmEmail(request, token):
    print("\n\t Token: ", token)
    print("\n\t request: ", request)

    new_user_details = Users.objects.last()
    firstname = new_user_details['firstname']
    lastname  = new_user_details['firstname']
    email     = new_user_details['email    ']

    template_name = 'emailconfirmation.html'
    context = {"firstname": firstname, 
                "lastname": lastname,
                "email": email}
    return render(request, template_name, context)