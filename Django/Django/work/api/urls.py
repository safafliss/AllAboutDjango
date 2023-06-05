from django.urls import path
from .views import  *

urlpatterns = [
    path('listJSON/' , getEvents),
    path('addList' , addEvent),
    path('updateEvent/<int:id>', updateEvent),
    path('deleteEvent/<int:id>', deleteEvent),
]
