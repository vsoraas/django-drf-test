from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from rest_framework import viewsets

from drf.models import HelloWorld
from drf.serializers import HelloSerializer


# ViewSets define the view behavior.
class HelloViewSet(viewsets.ModelViewSet):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloSerializer