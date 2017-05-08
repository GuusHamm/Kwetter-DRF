from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Kweet(models.Model):
    message = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('Account', related_name='kweets')

    def __str__(self):
        return "{0} - {1}".format(self.message, self.account)

