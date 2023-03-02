
from django.urls import path , re_path
from .views import *

urlpatterns = [
   
   #PreAuth Url's
    path('PreAuthForm', PreAuthFormView.as_view(), name='PreAuthForm'),
    path('PreAuthDocumentUpdate/<str:PreAuthID>', UpdatePreAuthDocumentView.as_view(), name='Update PreAuth Form'),
    path('ExistingPreAuthForm', ExistingPreAuthFormView.as_view(), name='Existing PreAuth Form'),
    path('DeletePreAuth<str:PreAuthID>', DeletePreAUth.as_view()),
    path('download_zip_files/<str:PreAuthID>',DownloadPreAuthZipFile.as_view(), name='download PreAuth zip files'),
    path('LinkingCaseNumber',LinkingCaseNumberView.as_view(), name='Link CaseNumber'),
    

    #Search Filters Url's
    re_path(r'SearchbyNHPMID/(?P<NHPMID>.+)$', FilterbyNHPMID.as_view(), name='Search by NHPMID'), 
    re_path(r'^SearchbyPreAuthID/(?P<PreAuthID>.+)$', SearchFilterbyPreAuthID.as_view(), name='Search by PreAuth-ID'),
    re_path(r'^SearchbyCaseNumber/(?P<CaseNumber>.+)$', SearchFilterbyCaseNumber.as_view() , name = 'Search by CaseNumber'),

    
    path('UploadShapeFile', UploadShapeFile.as_view(), name=' Upload ZIP file in database'),
    path('GetShapeFiles', ViewUploadedShapeFile.as_view(), name=' Get ZIP file'),
    path('delete/shapeFolder/<str:folder_name>', DeleteShapeFolder.as_view()),
  
    



]