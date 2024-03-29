# Generated by Django 4.2.1 on 2023-05-15 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_please_check_out_the_event_date_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check out the event date',
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 5, 15, 14, 31, 54, 757111))), name='Please check out the event date'),
        ),
    ]
