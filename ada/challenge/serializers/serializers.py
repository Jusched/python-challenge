# Django modules
from django.db.models import fields
from rest_framework import serializers

# Local modules
from ..models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model= Booking
        fields = '__all__'