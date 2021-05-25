from pstc.codes import SALARY_TABLES
from commndata.models import TimeLinedTable
from django.db import models
from django.utils.translation import gettext_lazy as _


class SalaryTable(TimeLinedTable):
    salary_table = models.CharField(max_length=10, verbose_name=_('salary table')
                                , choices=SALARY_TABLES)                            # 俸給表
    salary_level = models.IntegerField(verbose_name=_('salary level'))              # 級
    salary_no = models.IntegerField(verbose_name=_('salary no'))                    # 号俸
    salary_monthly = models.IntegerField(verbose_name=_('salary monthly'))          # 俸給月額
    salary_adjustment = models.IntegerField(verbose_name=_('salary adjustment'))    # 俸給の調整額
    
    class Meta:
        permissions = [
            ('import_salary_table', 'Can import salary_table'),
            ('export_salary_table', 'Can export salary_table'),
        ]
        verbose_name = _('salary table')
        verbose_name_plural = _('salary table')
        constraints = [
            models.UniqueConstraint(name='salary_table_unique', fields = ['start_date', 'salary_table', 'salary_level', 'salary_adjustment']), 
        ]
        ordering = ['-start_date', 'salary_table', 'salary_level', 'salary_no']
    
    def __str__(self):
        return self.salary_table
