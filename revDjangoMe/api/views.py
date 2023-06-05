from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from event.models import Event
from .serializer import EventSerializer

@api_view(['GET'])
def getEvents(request):
      events = Event.objects.all()
      serializer = EventSerializer(events , many=True)
      return Response(serializer.data ,status=status.HTTP_200_OK )
  
  
  
@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT'])
def updateEvent(request , id= None):
    event = Event.objects.get(id=id)
    serializer = EventSerializer(instance=event,data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def deleteEvent(request, id=None):
    try:
        event = Event.objects.get(id=id)
    except event.DoesNotExist:
        return Response(status="Event not found")
    event.delete()
    return Response("Event deleted")












@api_view(['GET'])
def getEvent(request, id=None):
    event = Event.objects.get(id=id)
    serializer = EventSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    paginator = CustomPagination()
    paginated_events = paginator.paginate_queryset(events, request)
    serializer = EventSerializer(paginated_events, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def getEvents(request):
    category = request.query_params.get('category', None)
    events = Event.objects.all()
    if category:
        events = events.filter(category=category)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
