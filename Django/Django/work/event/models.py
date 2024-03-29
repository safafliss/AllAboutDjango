from django.db import models
from datetime import datetime
from person.models import Person
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
def is_date_event(value):
    if value <= timezone.now():
        raise ValidationError(
            'event date must be greater than the current date')
    return value


class Event(models.Model):

    category_list = (
        ("Musique", "Musique"),
        ("Sport", "Sport"),
        ("Cinema", "Cinema")
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.CharField(choices=category_list, max_length=10)
    state = models.BooleanField(default=False)
    nbr_participant = models.IntegerField(default=0)
    evt_date = models.DateTimeField(null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    #hedhya paricipant mt3 table association many to many
    participant = models.ManyToManyField(
        Person,  through='participants', related_name="participant")
    #hedhya 5ater many to 1 lezm dima foregin key we nsmiwah organisateur 5ater hwua heka ch7atet fe schema
    organisateur = models.ForeignKey(
        Person, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    evt_date__gte=datetime.now()
                ),
                name='Please check out the event date'
            ),
        ]

#hedhiya el class association fiha 2 FK mt3 el person wel event
class participants(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_participation = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = [['person', 'evenement']]