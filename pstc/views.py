from django.urls.base import reverse_lazy
from keju.views import KejuContextMixin
from django.views.generic.base import TemplateView

from commndata.views import UploadView
from openpyxl import load_workbook

# Create your views here.
class KejuTemplateView(KejuContextMixin, TemplateView):
    template_name = "pstc/index.html"

class PstUploadView(KejuContextMixin, UploadView):
    success_url = reverse_lazy('pstc-site')

    def post(self, request, *args, **kwargs):
        form = self.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = form.cleaned_data['upload_file']
            wb = load_workbook(upload_file)
        
        return super().post(request, args, kwargs)