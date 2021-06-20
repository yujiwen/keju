from commndata.models import TimeLinedTable
from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum


class SalaryTable(TimeLinedTable):
    class SALARY_TABLE(models.IntegerChoices):
        GS1 = (1010, '行（一）')
        GS2 = (1020, '行（二）')
        SGS = (1110, '専門行政')
        ZM  = (1210, '税務')
        KA1 = (1310, '公安（一）')
        KA2 = (1320, '公安（二）')
        KJ1 = (1410, '海（一）')
        KJ2 = (1420, '海（二）')
        KI1 = (1510, '教（一）')
        KI2 = (1520, '教（二）')
        KK  = (1610, '研究')
        IR1 = (1710, '医（一）')
        IR2 = (1720, '医（二）')
        IR3 = (1730, '医（三）')
        FS  = (1810, '福祉')
        NK1 = (1910, '任研（一）')       # 任期付き研究員
        NK2 = (1920, '任研（二）')
        TNK = (1930, '特任研')           # 特定任期付き研究員
        SS  = (2010, '専門スタッフ')
        ST  = (2110, '指定職')           # 指定職

    class STAFF_TYPE(models.IntegerChoices):
        TY  = (1, '定員')
        SNY = (2, '再任用')

    salary_table = models.IntegerField(verbose_name=_('salary table'), blank=False,
        choices=SALARY_TABLE.choices, default=SALARY_TABLE.GS1)                     # 俸給表
    salary_level = models.IntegerField(verbose_name=_('salary level'))              # 級
    salary_no = models.IntegerField(verbose_name=_('salary no'))                    # 号俸
    salary_monthly = models.IntegerField(verbose_name=_('salary monthly'))          # 俸給月額
    salary_adjustment = models.IntegerField(verbose_name=_('salary adjustment'))    # 俸給の調整額
    
    @property
    def sny_salary_no():
        """
        再任用職員の号俸
        """
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
    salary_table = models.IntegerField(verbose_name=_('salary table'), blank=False,
        choices=SalaryTable.SALARY_TABLE.choices, default=SalaryTable.SALARY_TABLE.GS1)                     # 俸給表
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
