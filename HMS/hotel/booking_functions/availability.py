import datetime
from hotel.models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    Booking_list = Booking.obj.filer(room=room)

    # check if there is any booking in between check_in and check_out
    for booking in Booking_list:
        if (booking.check_in > check_out ) or (booking.check_out < check_in):
            avail_list.append(True)
        else:
            avail_list.append(False)
    
    # if there is no booking in between check_in and check_out, then the room is available, return True or False
    return all(avail_list)