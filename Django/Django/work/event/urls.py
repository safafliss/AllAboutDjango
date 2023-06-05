from django.urls import path

from .views import *
urlpatterns = [
    path('event/<str:name>', index),
    path('', list_event),
    path('list/', ListEvents.as_view(), name="Affiche"),
    path('detailsfct/<int:id>', eventDetails, name="details"), #te5dem
    #path('details/<int:pk>', DetailsEvent.as_view(), name="details"), #mayjiblich les données
    path('add/', AddEv, name="add"),
    path('update/<int:pk>', ModifierEvenement.as_view(), name="ModifierEvenement"),
    path('delete/<int:pk>', DeleteEvent.as_view(), name="deleteEvent"),
    path('participer/<int:event_id>', participer, name="participer"),
    path('cancel/<int:event_id>', cancel, name="cancel"),
]
