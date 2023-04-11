from django.contrib import admin
from . models import *

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=['name','email','password']
admin.site.register(student,studentAdmin)
