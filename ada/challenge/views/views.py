# Django and Django Rest modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import Http404

# Local modules
from ..models import Booking
from ..serializers import BookingSerializer


class BookingView:

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class BookingDetail:
    def get_object(self, pk):
        """Retrieve, update or delete."""

        try:
            bookings = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)

        return Response(serializer.data)

    def put(self, request, pk):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
