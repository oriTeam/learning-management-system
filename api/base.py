from django.views import View
from django.http import JsonResponse


class BaseManageView(View):
    """
    The base class for ManageViews
    A ManageView is a view which is used to dispatch the requests to the appropriate views
    This is done so that we can use one URL with different methods (GET, PUT, etc)
    """
    error_messages = {}
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method](request, *args, **kwargs)
        return JsonResponse({},status = 405)

    def json_error(self, field, code):
        default_errors = self.error_messages[field]
        errors = []
        errors.append({"code" : code, "message" : default_errors[code]})
        return JsonResponse({field : errors}, safe = False, status = 404)
    
