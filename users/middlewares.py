from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class CustomAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'session') or not request.user.is_authenticated:
            return HttpResponse("Not Authorised", status=401)  
        response = self.get_response(request)
        return response
