from django.urls import path , re_path
from .views import *

urlpatterns = [    


    path('CaseSheetPost', CaseSheetPostForm.as_view(), name='CaseSheetPost Claim Form'),
    path('LabtestPost', LabtestPostForm.as_view(), name='LabtestPost Claim Form'),
    path('ReportsPost', ReportsPostForm.as_view(), name='ReportsPost Claim Form'),
    path('DischargeSummaryPost', DischargesummuryPostAPI.as_view(), name='ReportsPost Claim Form'),
    path('DeathSummuryPost', DeathSummuryPostAPI.as_view(), name='DeathSummury Claim Form'),
    

    path('BloodDocumentsPost', BloodDocumentsPostAPi.as_view(), name='Blood Documents Claim Form'),

    path('MergeExcelFiles', ExcelMergexlsAPIView.as_view(), name='Merge Excel Files '),
    path('xls_ExcelUpload', DumpExcelInsertxls.as_view(), name='Excel Upload in database'),
    path('xlsx_ExcelUpload', DumpExcelInsertxlsx.as_view(), name='Excel Upload in database'),
    path('MPClaimPiad_ExcelUpload', MPClaimPiadPostApi.as_view(), name='Excel Upload in database'),

]