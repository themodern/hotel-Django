from django.db import models
#add new import 
from django.conf import settings
# Create your models here.
# create room and model 

class Room(models.Model):
    ROOM_CATEGORIES=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    
    number = models.CharField(max_length=200)
    categories = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

# this will display in admin panel if a new rooom obj is added
    def __str__(self):
        return f'{self.number}. {self.categories} with {self.beds} beds for {self.capacity} people'
    

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} for {self.room} guests from {self.check_in} to {self.check_out}'
    
