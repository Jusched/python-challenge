from django.db import models


class Booking(models.Model):
    """Booking model."""
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    origin= models.CharField(max_length=15)
    destination= models.CharField(max_length=15)
    departure_date= models.DateField()
    time_departure= models.TimeField()
    duration= models.TimeField()


    def __str__(self):
        return f'Booking made by {self.name}, on {self.origin}, in order to go to {self.destination} on {self.departure_date} at {self.time_departure} for {self.duration}'