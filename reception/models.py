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

    def __str__(self):
        return f"This is room number: {self.room_number} \n room status: {self.room_status}."

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
    
    firstname        = models.CharField(max_length=30)
    lastname         = models.CharField(max_length=30)

    email            = models.EmailField(unique=True)
    phone            = models.CharField(max_length=11, unique=True, error_messages={'unique':
                        "This phone field must contain only numbers of eleven characters."})
    
    checked_in       = models.BooleanField(default=False)
    duration         = models.PositiveIntegerField(editable=True, default=1)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.duration}."



class PaymentDetails(models.Model):
    """
    Model particulars for payment details by an occupant for a room.
    """
    room             = models.OneToOneField(Room, related_name='room',
                                             on_delete=models.DO_NOTHING)
    Occupant         = models.OneToOneField(Occupant, related_name='occupant',
                                             on_delete=models.DO_NOTHING)

    payment_status   = models.BooleanField(default=False)
    payment_date     = models.DateTimeField(auto_now_add=True)

    check_in_date    = models.DateTimeField(auto_now_add=True)
    check_out_date   = models.DateTimeField(editable=True, auto_now=True)
    



class ContactUs(models.Model):
    """
    Model to receive customer enquiries or complaints.
    """
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.EmailField()
    phone     = models.PositiveIntegerField()
    message   = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} from {self.firstname} {self.lastname}."




