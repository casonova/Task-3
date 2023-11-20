from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from users.models import User


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
