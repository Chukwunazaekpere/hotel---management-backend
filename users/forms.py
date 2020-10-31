from django import forms
from django.contrib.auth.forms import UserChangeForm

from allauth.account.forms import SignupForm as AllauthSignupForm
from allauth.account.adapter import get_adapter
from .models import Users


class SignupForm(AllauthSignupForm):
    def save(self, request):
        adapter = get_adapter()
        newUser = adapter.new_user(request)
        adapter.save(request, newUser, self)
        
        return newUser

class ChangeDetails(UserChangeForm):
    class Meta:
        model = Users
        fields = ['email']
