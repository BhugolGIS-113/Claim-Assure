
from django.urls import path , re_path
from .views import *

urlpatterns = [
    # path('compress-pdf', ImagePDFView.as_view(), name='compress_pdf'),
    path('PreAuthForm', PreAuthFormView.as_view(), name='PreAuthForm'),
    path('PreAuthDocumentUpdate/<str:PreAuthID>', UpdatePreAuthDocumentView.as_view(), name='PreAuthForm'),
    path('ExistingPreAuthForm', ExistingPreAuthFormView.as_view(), name='PreAuthForm'),
    path('DeletePreAuth<str:PreAuthID>', DeletePreAUth.as_view()),
    re_path(r'SearchbyNHPMID/(?P<NHPMID>.+)$', FilterbyNHPMID.as_view(), name='PreAuthForm'), 
    re_path(r'^SearchbyPreAuthID/(?P<PreAuthID>.+)$', SearchFilterbyPreAuthID.as_view(), name='PreAuthForm'),
    re_path(r'^SearchbyCaseNumber/(?P<CaseNumber>.+)$', SearchFilterbyCaseNumber.as_view()),
    path('download_zip_files/<str:PreAuthID>',DownloadPreAuthZipFile.as_view(), name='PreAuthForm'),
    path('LinkingCaseNumber',LinkingCaseNumberView.as_view(), name='PreAuthForm'),
    
    # path('PreAuthDocumentUpdate/<str:PreAuthID>',PreAuthDocumentUpdateAPIView.as_view(), name='PreAuthForm'),
    path('MergeExcelFiles', ExcelMergeAPIView.as_view(), name='PreAuthForm'),
    # path('api/latest-data/', LatestUploadsAPIView.as_view(), name='latest_data'),
    path('ClaimForm', ClaimFormView.as_view(), name='PreAuthForm'),
    path('ExcelUpload', DumpExcelInsert.as_view(), name='PreAuthForm'),
    



]