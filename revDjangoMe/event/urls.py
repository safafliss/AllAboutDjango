from django.urls import path

from .views import *
urlpatterns = [
    path('event/<str:name>', index),
    path('', list_event),
    path('list/', ListEvents.as_view(), name="Affiche"),
    path('detailsfct/<int:id>', eventDetails, name="details"), 
    #path('details/<int:pk>', DetailsEvent.as_view(), name="details"), 
    #path('add/', AddEv, name="add"),
    path('addClass/', AddEvent.as_view(), name="add"),
    path('updatefct/<int:pk>', modifier_evenement, name="ModifierEvenement"), 
    #path('update/<int:pk>', ModifierEvenement.as_view(), name="ModifierEvenement"),
    path('supprimer/<int:pk>', supprimer_evenement, name='deleteEvent'),
    #path('delete/<int:pk>', DeleteEvent.as_view(), name="deleteEvent"),
    path('participer/<int:event_id>', participer, name="participer"),
    path('cancel/<int:event_id>', cancel, name="cancel"),
]
