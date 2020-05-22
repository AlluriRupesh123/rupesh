from django.db import models

# Create your models here.
class rupi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(default=0)
    tz = models.CharField(max_length=100)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)
    start_times = models.DateField(null=True)
    end_times = models.DateField(null=True)


