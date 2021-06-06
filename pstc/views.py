from django.urls.base import reverse_lazy
from keju.views import KejuContextMixin
from django.views.generic.base import TemplateView

from commndata.views import UploadView


# Create your views here.
class KejuTemplateView(KejuContextMixin, TemplateView):
    template_name = "pstc/index.html"

class PstUploadView(KejuContextMixin, UploadView):
    success_url = reverse_lazy('pstc-site')
