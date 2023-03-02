from django.urls import path , re_path
from .views import *

urlpatterns = [    


    path('ClaimForm', ClaimFormView.as_view(), name='Post Claim Form'),
    path('MergeExcelFiles', ExcelMergeCSVAPIView.as_view(), name='Merge Excel Files '),
    path('ExcelUpload', DumpExcelInsert.as_view(), name='Excel Upload in database'),

]