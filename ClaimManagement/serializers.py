from rest_framework import serializers
from .models import *


class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField()


class CaseSheetSerializer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model =  CaseSheet
        fields = ( 'CaseNumberID','CaseNumber','AdmitCase_ClinicalSheet' , 'ICP' , 'MedicationChart' ,'InitialSheet' ,
                     'TPRChart' , 'VitalChart' , 'LOS_StayChart' , 'OtherDocuments')
        

class LabTestSerializer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model = LabTest
        fields = ( 'CaseNumberID' ,'CaseNumber', 'Microbiology' ,'Biochemistry' , 'Pathology' ,'SerologyInvestigation' , 'OtherDocuments')

class ReportsSerializer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model = Reports
        fields = ( 'CaseNumberID' , 'CaseNumber' , 'Radiology' , 'OT_ProcedureSheets' , 'AnaesthesiaNotes' , 'AnaesthesiaNotes' , 'OtherDocuments')


class DischargeSummarySerialzer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model = DischargeSummary
        fields = ('CaseNumberID' , 'CaseNumber' , 'dischargeDate' , 'DischargeType' , 'DischargeSummaryDocument' , 'OtherDocuments')

class DeathSummarySerialzer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model = DeathSummary
        fields = ('CaseNumberID' , 'CaseNumber' , 'MortalityAudit' ,'DeathCertificate',
                  'OtherDocuments')

class BloodDocumentsSerializer(serializers.ModelSerializer):
    CaseNumber = serializers.CharField(max_length=100 , required=True)
    class Meta:
        model = BloodDocuments
        fields = ('CaseNumberID' , 'CaseNumber' , 'BloodTransfusion' , 'BTSticker' , 'CrossMatchReport' , 'OtherDocuments')
class DumpExcelSerializer(serializers.Serializer):
    excel_file = serializers.FileField(required=True)

class DumpCSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField(required=True)
