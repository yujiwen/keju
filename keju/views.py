from django.views.generic.base import ContextMixin, View
from django.utils.translation import gettext_lazy as _


class KejuContextMixin(ContextMixin):
    site_title = _('keju')
    site_header = _('keju')
    site_url = '/keju'

    enable_nav_sidebar = False
    
    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active

    def each_context(self, request):
        """
        Return a dictionary of variables to put in the template context for
        *every* page in the site.
        For sites running on a subpath, use the SCRIPT_NAME value if site_url
        hasn't been customized.
        """
        script_name = request.META['SCRIPT_NAME']
        site_url = script_name if self.site_url == '/' and script_name else self.site_url
        return {
            'site_title': self.site_title,
            'site_header': self.site_header,
            'site_url': site_url,
            'has_permission': self.has_permission(request),
            'is_popup': False,
            'is_nav_sidebar_enabled': self.enable_nav_sidebar,
        }

    def get_context_data(self, **kwargs):
        if not hasattr(self, 'request'):
            raise AttributeError(
                "%s instance has no 'request' attribute. Did you override "
                "setup() and forget to call super()?" % self.__class__.__name__
            )

        return self.each_context(self.request) | super(KejuContextMixin, self).get_context_data(**kwargs)
