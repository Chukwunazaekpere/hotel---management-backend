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

from django.views.generic import (
    DetailView
)

from .serializers import (
    RoomSerializer, OccupantSerializer, ContactSerializer
)

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings 
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'index.html'

