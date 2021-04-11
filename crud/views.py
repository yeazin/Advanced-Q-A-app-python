from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Question, Quser,Topics
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator

class HomeApp(View):

    def get(self, request, *args, **kwargs):
        question_obj = Question.objects.all().order_by('-id')
        topics_obj = Topics.objects.all().order_by('-id')
        paginator = Paginator(question_obj, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'question':question_obj,
            'topics':topics_obj
        }
        return render (request, 'home/app.html', context)
        
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

class CreateUser(View):
    def get(self,request, *args, **kwargs):
        return render (request,'user/create_user.html')
    def post(self, request, *args,**kwargs):
        data = request.POST
        email = data.get('email')
        username = data.get('username')
        image = request.FILES.get('image')
        #bio = data.get('bio')
        password1 = data.get('password1')
        password2 = data.get('password2')
        user = User.objects.all().filter(username=username)
        if user:
            messages.warning(request,'Username Already Exits!')
            return redirect('create_user')
        elif password1 != password2:
            messages.info(request, 'Password Didnot Match')
            return redirect ('create_user')
        else:
            auth_info = {
            'username':username,
            'password':make_password(password1)

            }
            user = User(**auth_info)
            user.save() 
        user_obj = Todouser(user=user,email=email)
        user_obj.save(Todouser)
        messages.success(request,'Thanks for Sign In')
        return redirect('dashboard')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html')
    def post(self, request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sorry! username or password didn`t match')
            return redirect('login')

class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        logout(request)
        return redirect('login')

class DashboardView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        current_user = request.user
        user_q = Question.objects.all().filter(user=request.user)
        context={
            'user':current_user
        }
        return render(request, 'user/dashboard.html', context)
