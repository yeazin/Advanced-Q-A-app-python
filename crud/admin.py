from django.contrib import admin
from .models import ToDo,Todouser

# Register your models here.

admin.site.register(ToDo)
admin.site.register(Todouser)