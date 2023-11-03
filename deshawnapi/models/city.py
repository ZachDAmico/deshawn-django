# import base class from Django stdlib
from django.db import models

# only name property defined here because Django auto creates id column, makes it pk, and set it to autoincrement whenever new row inserted
# this has to inherit from this base class(models.Model)
class City(models.Model): 
    # must define all non-id fields
    name = models.CharField(max_length=155)

