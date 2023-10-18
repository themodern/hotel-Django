import datetime
from hotel.models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    Booking_list = Booking.objects.filter(room=room)
    for booking in Booking_list:
        if (booking.check_in > check_out )or (booking.check_out < check_in):
            avail_list.append(True)
        else:
            avail_list.append(False)
            
    # check if all the items in avail_list are True
    return all(avail_list) 