from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from users.models import User
from datetime import datetime
import os
from CustomAuthentication.settings import BASE_DIR

class CustomAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.method == "POST":
                email = request.POST.get('username')
                password = request.POST.get('password')
                user = self.authenticate_user(email, password)
                if user is not None:
                    request.user = user 
                else:
                    return HttpResponse("Invalid Credentials")
        response = self.get_response(request)
        return response
    
    def authenticate_user(self, email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user     
            else:
                return None 
        except User.DoesNotExist:
            return None


class CustomLoggingMIddleware:
    def __init__(self,get_responce):
        self.get_response=get_responce
    
    def __call__(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR', '')
            
        requested_url = request.get_full_path()
        user = request.user
        log_data = f"Time: {datetime.now()} - IP Address: {ip_address} - URL_Path: {requested_url} - User: {user} \n"

        log_file_path = os.path.join(BASE_DIR,'request_logs.txt')
        with open(log_file_path, 'a') as log_file:
            log_file.write(log_data)
            
        response = self.get_response(request)
        return response
        
        
        
        
            