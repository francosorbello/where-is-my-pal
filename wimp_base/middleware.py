from django.conf import settings
from django.utils import translation
from wimp_base.models import SiteSettings


class AdminLanguageMiddleware:
    """
    Middleware that forces the language based on SiteSettings in the database.
    Admins can change the language via the admin page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            site_settings = SiteSettings.get_settings()
            admin_language = site_settings.language
        except Exception:
            admin_language = getattr(settings, 'ADMIN_LANGUAGE', 'en')
        
        translation.activate(admin_language)
        request.LANGUAGE_CODE = admin_language
        
        response = self.get_response(request)
        
        return response
