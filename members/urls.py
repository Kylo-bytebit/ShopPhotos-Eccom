from django.urls import path
from . import views
from . views import profile


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user,name="logout"),
    path('register_user', views.register_user,name="register_user"),
    path('profile/', views.profile, name='profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
]