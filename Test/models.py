from django.db import models

# Install this to use MongoDB
from mongoengine import *
import datetime
# Create your models here.

class Vehicle(EmbeddedDocument):
    license_plate = StringField(max_length=200)
    brand = StringField(max_length=200)
    color = StringField(max_length=100)

class Driver(Document):
    firstname = StringField(max_length=200)
    lastname = StringField(max_length=200)
    birth_date = DateTimeField()
    creation_date = DateTimeField()
    modified_date = DateTimeField()
    vehicle = EmbeddedDocumentField(Vehicle)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Driver, self).save(*args, **kwargs)
