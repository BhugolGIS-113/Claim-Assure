from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(PreAuthDocument)
admin.site.register(PreAuthLinkCaseNumber)
admin.site.register(ClaimManagement)
admin.site.register(DumpExcel)