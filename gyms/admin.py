from django.contrib import admin

from gyms.models import Gym
from msystatistics.models import City, PropertyOwnership

# Register your models here.
admin.site.register(Gym)

admin.site.register(City)
admin.site.register(PropertyOwnership)