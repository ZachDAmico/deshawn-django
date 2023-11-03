"""Appointment database model module"""
from django.db import models


class Appointment(models.Model):
    """Database model for tracking walker appointments"""
    completed = models.BooleanField(default=False)
    date = models.DateField()
    walker = models.ForeignKey('Walker', on_delete=models.CASCADE, related_name='appointments')
    # ------THINGS TO TAKE NOTE OF------
    # to create walker_id fk, don't need to put _id in class definition -
    # django auto creates _id for foreign key to link each appt to a walker
    # default argument will auto set value to 0 when new row inserted,
    # here default is changed to be false
    # 'Walker' argument for fk is name of related class