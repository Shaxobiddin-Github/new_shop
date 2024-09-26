from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest 
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required,login_required
# Create your views here.

from .forms import RegisterForm,LoginForm



class HomeView(View):
    def get(self,request):
        return render(request, 'app/index.html')


    

from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'title': "Register",
            'image_url': "https://erkatoy.uz/images/Betta_test_sh/Robot_E_Bot.png",
            'form': form,  # Formani kontekstga qo'shamiz
        }
        return render(request, 'register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tabriklaymiz... Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")
            return redirect('login')
        
        # Agar forma invalid bo'lsa, uni qayta ko'rsatamiz
        context = {
            'title': "Register",
            'image_url': "https://erkatoy.uz/images/Betta_test_sh/Robot_E_Bot.png",
            'form': form,
        }
        return render(request, 'register.html', context)


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, 'login.html', context)
    
    def post(self,request:WSGIRequest):
        if request.method == "POST":
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user=login_form.get_user()
                login(request,user)
                messages.success(request, f"saytga xush kelibsiz {user.username}")
                return redirect('home')
        return render(request, 'login.html')
            

class LogoutView(View):
    
    def get(self,request):
        logout(request)
        messages.warning(request, "Siz saytdan muvaffaqiyatli chiqdingiz!!")
        return redirect('login')
    
    def post(self,request:WSGIRequest):
        logout(request)
        messages.warning(request, "Siz saytdan muvaffaqiyatli chiqdingiz!!")
        return redirect('login')