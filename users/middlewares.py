from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AuthenticationMIddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        print(user)
        if user.is_authenticated:
            return HttpResponse(status=200)
        else:
            return HttpResponse('Unauthorised', status=401)