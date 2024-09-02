from django.db import models


class Appointments(models.Model):
    fullname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.fullname
