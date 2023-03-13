from django.contrib import admin
from django.urls import path , include
from rest_framework import permissions
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Claim Assure",
      default_version='v1',
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/Auth/', include('Authentications.urls')),
    path('api/PreAuth/', include('PreAuth.urls')),
    path('api/Claim/', include('ClaimManagement.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
