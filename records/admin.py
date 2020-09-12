from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Staging
import pandas as pd
# Register your models here.

@admin.register(Staging)
class PersonAdmin(ImportExportModelAdmin):
    pass
    # data = pd.read_excel(r"D:\validation_test.xlsx")
    #
    # list_disp = list(data.columns)
