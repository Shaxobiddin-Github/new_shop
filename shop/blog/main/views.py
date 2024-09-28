from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest 
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .forms import RegisterForm,LoginForm



class HomeView(View):
    # @login_required(login_url="login.html")
    def get(self,request):
        return render(request, 'main/index.html')





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
                print(user.username,user.password  )
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


class ProfileView(View):

    def get(self, request):
        return render(request, 'profile.html')
    
    def post(self, request:WSGIRequest):
        if request.user.is_authenticated:
            user = request.user
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.phone_number = request.POST['phone_number']
            user.save()
        return redirect('profile')


    

class UpdateProfileImageView(LoginRequiredMixin, View):
    def post(self, request):
        if 'image' in request.FILES:
            image = request.FILES['image']
            if image.name.endswith(('.jpg', '.jpeg', '.png')):
                user = request.user
                user.image = image
                user.save()
                messages.success(request, 'Profil rasmi o\'zgartirildi!')
            else:
                messages.error(request, 'Noto\'g\'ri fayl formati. JPG, JPEG yoki PNG formatidagi rasmni tanlang.')
                return redirect('profile')
        messages.error(request, 'Rasmni yuklashda xato!')
        return redirect('profile')
