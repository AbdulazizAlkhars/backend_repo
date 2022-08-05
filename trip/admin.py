from django.contrib import admin

# Register your models here.

from trip import models

to_register =[
    models.UserProfile,
    models.Trip,
]

admin.site.register(to_register)