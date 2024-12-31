from django.conf import settings


class AdminCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If URL starts with /admin --> use different cookie
        if request.path.startswith('/admin'):
            settings.SESSION_COOKIE_NAME = 'admin_sessionid'
        else:
            settings.SESSION_COOKIE_NAME = 'sessionid'
        return self.get_response(request)
