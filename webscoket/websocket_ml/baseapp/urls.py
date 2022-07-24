from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/youtube/v1',  YoutubeAPI.as_view(), name='youtubeAPI'),
    path('api/calendar/v1',  CalendarAPI.as_view(), name='calendarAPI'),
    path('test', TestView.as_view()),
    path('turnitin/', TurnitinView.as_view())

]
