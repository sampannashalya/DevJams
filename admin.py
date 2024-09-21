from django.contrib import admin
from .models import TeachingRegistration,VolenteerRegistration,Choice,Education

admin.site.register(TeachingRegistration)
admin.site.register(Choice)
admin.site.register(Education)
admin.site.register(VolenteerRegistration)
# Register your models here.
