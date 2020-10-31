from django.db import models
from django.urls import reverse


class Room(models.Model):
    """
    Model features for a room.
    """
    roomType = (
        ('Executive', 'executive'),
        ('Business', 'business'),
        ('Convalescence', 'executive'),
    )

    roomStatus = (
        ('Occupied', 'Occupied'),
        ('Free', 'Free'),
        ('Booked', 'Booked'),
    )

    room_type   = models.CharField(max_length=30, choices=roomType, default='Business')
    room_price  = models.DecimalField(max_digits=8, decimal_places=2)
    room_number = models.PositiveIntegerField()
    room_status = models.CharField(max_length=10, choices=roomStatus, blank=True, default=True)
    slug        = models.SlugField(blank=True)

    def get_absolute_url(self):
        # return room details
        return reverse(('room:room_details'), args=[self.slug])

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = '-'.join([self.room_type, str(self.room_number)])
        if not self.room_status:
            print("\n\t args: ", args)
            print("\n\t kwargs: ", kwargs)
        super().save(*args, **kwargs)


class Occupant(models.Model):
    """
    Model for room occupant
    """
    # Make a one to one field to map occupants to room; since rooms
    # will be constant but occupants aren't.
    room             = models.OneToOneField(Room, related_name='room',
                                             on_delete=models.DO_NOTHING)
    firstname        = models.CharField(max_length=30)
    lastname         = models.CharField(max_length=30)

    username         = models.CharField(max_length=100, blank=True)
    email            = models.EmailField()
    phone            = models.CharField(max_length=11, error_messages={'unique':
                        "This phone field must contain only numbers of eleven characters."})
    
    payment_status   = models.BooleanField(default=False)
    check_in_date    = models.DateTimeField(auto_now_add=True)
    duration         = models.PositiveIntegerField(editable=True, default=1)
    check_out_date   = models.DateTimeField(editable=True, auto_now=True)

    def save(self, *args, **kwargs):
        paid = kwargs['paid']
        if paid:
            self.payment_status = True
            new_room_reservation = Room()
            new_room_reservation.save('Booked')
            # new_room_reservation.save()
            print("\n\t args: ", args)
            print("\n\t kwargs: ", kwargs)
        super().save(*args, **kwargs)


        




