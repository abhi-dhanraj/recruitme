from django.contrib import admin

# Register your models here.
from .models import application,rounds,process

admin.site.register(application)
admin.site.register(rounds)
admin.site.register(process)