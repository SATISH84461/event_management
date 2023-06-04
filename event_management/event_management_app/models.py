from django.db import models
from django.contrib.auth.models import User

# this model will store the event details
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    date = models.DateField(max_length=256)
    start_time = models.TimeField(max_length=256)
    end_time = models.TimeField(max_length=256)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

# this will store the details of user who have register for which event
class Event_User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'event')) # make composite key(combination of user and event must be unique)

