from django.contrib import admin
from .models import Question,Quser, Topics

# Register your models here.

admin.site.register(Question)
admin.site.register(Quser)
admin.site.register(Topics)