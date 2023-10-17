from django.db import models

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