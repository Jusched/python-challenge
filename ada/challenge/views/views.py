# Django and Django Rest modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.shortcuts import get_object_or_404

# Local modules
from ..models import Booking
from ..serializers import BookingSerializer


@api_view(["GET"])
def ApiView(request):
    api_urls= {
        'View': "view/pk/",
        'Add': 'create/',
        'Update': 'update/pk/',
        'Delete': 'delete/pk/',
    }
    
    return Response(api_urls)


@api_view(["GET"])
def view_booking(request, pk):

    booking = Booking.objects.get(pk=pk)
    serializer = BookingSerializer(booking)

    if booking:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_booking(request):

    booking = BookingSerializer(data=request.data)

    if Booking.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This booking already exists.")

    if booking.is_valid():
        booking.save()
        return Response(booking.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_booking(request, pk):

    booking= Booking.objects.get(pk=pk)
    data= BookingSerializer(instance=booking, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_booking(request, pk):

    booking= get_object_or_404(Booking, pk=pk)
    booking.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

