from django.urls import path
from . import views

urlpatterns=[
    path('register',views.registration_form,name='register'),
    path('login',views.login_form,name='login'),
    path('logout',views.user_logout,name='logout'),
]
