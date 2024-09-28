from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('register/', RegisterView.as_view(), name ='register'),
    path('login/', LoginView.as_view(), name ='login'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('profile/', ProfileView.as_view(), name ='profile'),
    path('profile/', ProfileView.as_view(), name ='profile'),
    path('user/profile/update-photo/',UpdateProfileImageView.as_view(), name="update_photo"),
    # path('my_orders/', MyOrdersView.as_view(), name ='my_orders'),
    # path('my_favorites/', MyFavoritesView.as_view(), name ='my_favorites'),
    # path('my_addresses/', MyAddressesView.as_view(), name ='my_addresses'),

]
