from django.contrib import admin

# Register your models here.
from .models import applicant,institute

admin.site.register(applicant)
admin.site.register(institute)