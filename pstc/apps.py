from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PstcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pstc'
    verbose_name = _('pstc')
