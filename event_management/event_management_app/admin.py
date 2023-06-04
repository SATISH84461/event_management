from django.contrib import admin
from . import models

# registering Events model whcih contains list of all the Events
admin.site.register(models.Events)

# registering Event_User model whcih contains data that which user has register for which event
admin.site.register(models.Event_User)