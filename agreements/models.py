from django.db import models
from django.utils import timezone

# Create your models here.
class Agreement(models.Model):
    contractnumber = models.CharField(max_length=10)
    startdata = models.DateTimeField(default=timezone.now)
    subject = models.TextField()
    completdata = models.DateTimeField()
    department = models.CharField(max_length=20)
    profitable = models.BooleanField(default=False)
    autoprolongation = models.BooleanField(default=False)


