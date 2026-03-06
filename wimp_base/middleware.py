from django.conf import settings
from django.utils import translation


class AdminLanguageMiddleware:
    """
    Middleware that forces the language to be the ADMIN_LANGUAGE setting.
    This allows admins to configure the language statically in settings.py.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_language = getattr(settings, 'ADMIN_LANGUAGE', 'en')
        translation.activate(admin_language)
        request.LANGUAGE_CODE = admin_language
        
        response = self.get_response(request)
        
        return response
