from django.contrib import admin
from .models import JobAdvert, JobApplication

# Register your models here.

admin.site.register([JobAdvert, JobApplication])
