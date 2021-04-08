from django.shortcuts import render
from django.views import View
from .models import ToDo


class HomeApp(View):

    def get(self, request, *args, **kwargs):
        todo_obj = ToDo.objects.all().order_by('-id')
        context ={
            'todo':todo_obj
        }
        return render (request, 'index.html', context)
