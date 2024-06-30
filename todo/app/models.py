from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=30)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.id}>{self.name}'