from pstc.models import SalaryTable
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import models as auth
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

from checked_csv.admin import CsvExportModelMixin, CsvImportModelMixin
from commndata.models import CodeCategory, CodeMaster
from commndata.admin import BaseTableAdminMixin, TimeLinedTableAdminMixin, UserAdminMixin


class MasterAdminSite(admin.AdminSite):
    site_title = _('Master')
    site_header = _('Master Maintenance')
    site_url = '/keju'
    
    def index(self, request):
        context = {
            **self.each_context(request),
            'title': _('Master'),
            'app_list': self.get_app_list(request),
        }

        return render(request, 'pstc/master/index.html', context=context)

masterAdmin = MasterAdminSite(name='masterAdmin')

# Register your models here.

@admin.register(auth.Group, site=masterAdmin)
class GroupModelAdmin(CsvExportModelMixin, CsvImportModelMixin, GroupAdmin):
    pass

@admin.register(auth.User, site=masterAdmin)
class UserModelAdmin(UserAdminMixin, CsvExportModelMixin, CsvImportModelMixin, UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'is_superuser']
    # export_fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'is_superuser')

class CodeCategoryModelAdmin(BaseTableAdminMixin, CsvExportModelMixin, CsvImportModelMixin, ModelAdmin):
    # import_field_names = ['codecategory', 'name']
    pass

masterAdmin.register(CodeCategory, CodeCategoryModelAdmin)

@admin.register(CodeMaster, site=masterAdmin)
class CodeMasterModelAdmin(TimeLinedTableAdminMixin, CsvExportModelMixin, CsvImportModelMixin, ModelAdmin):
    list_display = ['codecategory', 'code', 'name', 'start_date', 'end_date']
    list_filter = ['codecategory__name', 'start_date']
    search_fields = ('codecategory__name', 'name')
    date_hierarchy = 'start_date'

    def get_readonly_fields(self, request, obj=None):
        fields = super(CodeMasterModelAdmin, self).get_readonly_fields(request, obj)
        if obj:
            return (*fields, 'codecategory')
        else:
            return fields

@admin.register(SalaryTable, site=masterAdmin)
class SalaryTableModelAdmin(TimeLinedTableAdminMixin, CsvExportModelMixin, CsvImportModelMixin, ModelAdmin):
    # export_fields = ('start_date', 'end_date', 'salary_table', 'salary_level', 'salary_no', 'salary_monthly', 'salary_adjustment')
    date_hierarchy = 'start_date'

