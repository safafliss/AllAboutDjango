# Generated by Django 4.1 on 2023-05-19 19:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Musique', 'Musique'), ('Sport', 'Sport'), ('Cinema', 'Cinema')], max_length=10)),
                ('state', models.BooleanField(default=False)),
                ('nbr_participant', models.IntegerField(default=0)),
                ('evt_date', models.DateTimeField(null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participation', models.DateTimeField(default=datetime.datetime.now)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
