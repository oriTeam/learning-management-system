from django.conf import settings
from django.http import QueryDict
 
class HttpPostTunnelingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if 'HTTP_X_METHOD_OVERRIDE' in request.META:
            if 'csrfmiddlewaretoken' in request.POST:
                request.META.setdefault('HTTP_X_CSRFTOKEN', request.POST['csrfmiddlewaretoken'])
            http_method = request.META['HTTP_X_METHOD_OVERRIDE']
            if http_method.lower() == 'put':
                request.method = 'PUT'
                request.META['REQUEST_METHOD'] = 'PUT'
                request.PUT = QueryDict(request.body)
            if http_method.lower() == 'delete':
                request.method = 'DELETE'
                request.META['REQUEST_METHOD'] = 'DELETE'
                request.DELETE = QueryDict(request.body)
        return None

class CORSMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = settings.FRONTEND_SERVER_URL

        return response

