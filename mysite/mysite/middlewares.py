from django.http import HttpResponseForbidden

class BlockStaticMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/static/txt/flag.txt'):
            return HttpResponseForbidden()
        response = self.get_response(request)
        return response

