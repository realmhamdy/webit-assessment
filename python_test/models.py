from django.db import models


class Address(models.Model):

    street_name = models.CharField(max_length=32, null=True)
    suburb = models.CharField(max_length=32, null=True, db_index=True)
    postcode = models.CharField(max_length=16, null=True)
    state = models.CharField(max_length=32, null=True)


class Client(models.Model):

    name = models.CharField(max_length=64, null=False, blank=False, db_index=True, unique=True)
    address = models.OneToOneField(Address, related_name="client", on_delete=models.SET_NULL, null=True)
    contact_name = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=False, unique=True, db_index=True)
    phone = models.CharField(max_length=16, null=True)
