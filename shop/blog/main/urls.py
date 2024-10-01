from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('register/', RegisterView.as_view(), name ='register'),
    path('login/', LoginView.as_view(), name ='login'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('profile/', ProfileView.as_view(), name ='profile'),
    path('profile/', ProfileView.as_view(), name ='profile'),
    path('user/profile/update-photo/',UpdateProfileImageView.as_view(), name="update_photo"),
    path('user/profile/change_password/', CustomerChangePassword.as_view(), name ='change_password'),

    path('reset-password/', PasswordResetView.as_view(), name ='reset_password'),
    path('reset/<uidb64>/<token>', PasswordResetView.as_view(), name ='password_reset_confirm'),
    path('reset-password-done/', PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset-password-complate/', PasswordResetCompleteView.as_view(), name ='password_reset_complate'),
    # path('my_addresses/', MyAddressesView.as_view(), name ='my_addresses'),

]
