from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('reset_pass',views.reset_pass,name='reset_pass'),
]
