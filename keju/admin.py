from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

from commndata.admin import ActiveUserAdminSite


class KejuAdminSite(ActiveUserAdminSite):
    site_title = _('keju')
    site_header = _('keju')
    site_url = '/keju'

    index_title = _('keju')

    def index(self, request):
        context = {
            **self.each_context(request),
            'title': _('home'),
            'app_list': self.get_app_list(request),
        }

        return render(request, 'keju/index.html', context=context)


admin.site = KejuAdminSite()
