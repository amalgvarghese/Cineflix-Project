from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Movie)

admin.site.register(models.Industry)

admin.site.register(models.Genre)

admin.site.register(models.Artist)

admin.site.register(models.Language)