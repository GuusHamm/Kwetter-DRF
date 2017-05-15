from django.db import models


# Create your models here.

class Kweet(models.Model):
    message = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('account.Account', related_name='kweets')

    def __str__(self):
        return "{0} - {1}".format(self.message, self.account)



