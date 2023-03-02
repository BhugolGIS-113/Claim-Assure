from rest_framework import serializers
from .models import *


class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField()


class ClaimFormSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ClaimManagement
        fields = ( 'CaseNumberID','CaseNumber','AdmitCase_ClinicalSheet' , 'ICP' , 'MedicationChart' ,'InitialSheet' ,
                     'TPRChart' , 'VitalChart' , 'LOS_StayChart' , 'CaseSheets_OtheDocuments' , 'Microbiology',
                     'Biochemistry' , 'Pathology' , 'SerologyInvestigation' , 'Radiology' ,'OT_ProcedureSheets',
                     'AnaesthesiaNotes' , 'dischargeDate' , 'DischargeType' , 'DischargeSummaryDocument' , 'MortalityAudit', 'DeathCertificate',
                      'BloodTransfusion' , 'BTSticker' , 'CrossMatchReport' , 'OtherDocuments' ,'Status' )


class DumpExcelSerializer(serializers.Serializer):
    excel_file = serializers.FileField(required=True)
