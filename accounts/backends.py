from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import Account

class MyBackEnd(BaseBackend):
    def authenticate(self,request,email=None,password=None,**kwargs):
        try:
            user = Account.objects.get(email=email)
        except:
            return None
        
        if user.check_password(password):
            return user
        
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
         
         