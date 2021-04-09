from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import ToDo


class HomeApp(View):

    def get(self, request, *args, **kwargs):
        todo_obj = ToDo.objects.all().order_by('-id')
        paginator = Paginator(todo_obj, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'todo':page_obj
        }
        return render (request, 'index.html', context)
        
class CreateTodoView(View):

    def get(self, request, *args, **kwargs):
        return render (request, 'index.html')

    def post(self, request, *args, **kwargs):
        list_name = request.POST.get('todo')

        todo_obj = ToDo(list_name= list_name)
        todo_obj.save()
        return redirect ('home') 
    
class EditTodoView(View):

    def post(self, request,id,  *args, **kwargs):
        obj = get_object_or_404(ToDo, id=id )
        obj.list_name  = request.POST.get('todo')
        obj.save()
        return redirect('home')

class DeleteTodoView(View):

    def post(self, request, id, *args, **kwargs):
        obj = get_object_or_404(ToDo, id=id)
        obj.delete()
        return redirect('home')
