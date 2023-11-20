from django.contrib.auth.hashers import check_password
from users.models import User
from django.shortcuts import HttpResponse


class BackendAuthentication:
    def authenticate(email=None, password= None):
        try:
            user=User.objects.get(email=email)
                
            if check_password(password, user.password):
                return user
            else:
                return HttpResponse("User doesnot exist", status = 401)
        except User.DoesNotExist:
            return None    