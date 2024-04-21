from django.contrib import admin
from .models import Record # .models mean from the models.py file and Record is the class
# Register your models here.

admin.site.register(Record)