from pstc.salary_table_codes import SALARY_TABLES
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
    
    @property
    def sny_salary_no():
        return 999

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

class SalaryTableExcel(TimeLinedTable):
    salary_table = models.CharField(max_length=10, verbose_name=_('salary table')
                                , choices=SALARY_TABLES)                                # 俸給表
    sheet_name = models.CharField(max_length=10, verbose_name=_('シート名'))
    rows = models.IntegerField(verbose_name=_('級'), default=1)
    cols = models.IntegerField(verbose_name=_('号俸'), default=1)
    sny_flg = models.BooleanField(verbose_name=_('再任用有無'), default=True)
    start_cell = models.CharField(max_length=10, verbose_name=_('データ開始セル'))

    class Meta:
        db_table = 'salary_table_excel'
        verbose_name = _('俸給表取込エクセル設定')
        verbose_name_plural = _('俸給表取込エクセル設定')
        constraints = [
            models.UniqueConstraint(name='salary_table_excel_unique', fields = ['start_date', 'salary_table',]), 
        ]
        ordering = ['-start_date', 'salary_table', ]
