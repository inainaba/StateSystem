from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello")
