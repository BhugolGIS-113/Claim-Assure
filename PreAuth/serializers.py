from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()



class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class PreAuthDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreAuthDocument
        fields = '__all__'




class CombinedSerializer(serializers.Serializer):

    NHPMID = serializers.CharField(max_length=255, required=True)
    nameOfPatient = serializers.CharField(max_length=255, required=True)
    adharNumber = serializers.CharField(max_length=255, required=True)
    adharPhotograph = serializers.ImageField(required=  False)
    DOB = serializers.DateField(required = True )
    gender = serializers.CharField(max_length=255, required=True)
    mobileNumber = serializers.IntegerField(required = True)
    alternativeNumber = serializers.IntegerField(required = False) 
    addressLine1 = serializers.CharField(max_length=255, required=False)
    addressLine2 = serializers.CharField(max_length=255, required=False)
    district = serializers.CharField(max_length=255, required=False)
    pincode = serializers.IntegerField(required= False)
    RationCardNumber = serializers.CharField(max_length=20, required=False)
    RationCardPhotograph =  serializers.ImageField(required= False)
    
    dateOfAdmission = serializers.DateTimeField(required = True)
    dateOfPreAuth = serializers.DateTimeField(required = True)
    hospitalName = serializers.CharField(max_length=255, required = True)
    hospitalCode = serializers.CharField(max_length=255 , required  = True)
    justification = serializers.ImageField(required = False)
    on_BedPhotograph = serializers.ImageField(required = False)
    admitCaseSheet = serializers.ImageField(required = False)
    labReport = serializers.ImageField(required = False)
    radiologyReport = serializers.FileField(required = False)

    
class ExistingPreAuthserializer(serializers.ModelSerializer):
    class Meta:
        model = PreAuthDocument
        fields = ('PreAuthID','PersonalInfoID','dateOfAdmission' ,'dateOfPreAuth' , 'hospitalName' ,
                 'hospitalCode' , 'justification' , 'on_BedPhotograph' , 'admitCaseSheet', 'labReport', 'radiologyReport' ,)



class ExistingPreAuthDocumentSerializer(serializers.Serializer):
    PersonalInfoID = serializers.IntegerField(required=True)
    dateOfAdmission = serializers.DateTimeField(required = True)
    dateOfPreAuth = serializers.DateTimeField(required = True)
    hospitalName = serializers.CharField(max_length=255, required = True)
    hospitalCode = serializers.CharField(max_length=255 , required  = True)
    justification = serializers.ImageField(required = False)
    on_BedPhotograph = serializers.ImageField(required = False)
    admitCaseSheet = serializers.ImageField(required = False)
    labReport = serializers.ImageField(required = False)
    radiologyReport = serializers.FileField(required = False)



class ZipFileSerializer(serializers.ModelSerializer):
    zip_file = serializers.FileField()

    class Meta:
        model = PreAuthDocument
        fileds = ( 'id', 'justification')


class CaseNumberLinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAuthLinkCaseNumber
        fields = ('PreAuthID' , 'CaseNumber')


class PreAuthSearchDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAuthDocument
        fields = ('PersonalInfoID' , 'PreAuthID' , 'dateOfAdmission',
                  'dateOfPreAuth' , 'hospitalName' , 'hospitalCode' , 'justification',
                  'on_BedPhotograph' , 'admitCaseSheet' , 'labReport' , 'radiologyReport' )


class PreAuthSearchDocumentUpdateSerializer(serializers.Serializer):
    dateOfAdmission = serializers.DateTimeField(required = True)
    dateOfPreAuth = serializers.DateTimeField(required = True)
    hospitalName = serializers.CharField(max_length=255, required = True)
    hospitalCode = serializers.CharField(max_length=255 , required  = True)
    justification = serializers.ImageField(required = False)
    on_BedPhotograph = serializers.ImageField(required = False)
    admitCaseSheet = serializers.ImageField(required = False)
    labReport = serializers.ImageField(required = False)
    radiologyReport = serializers.FileField(required = False)



class preauth_document_serializer_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = PreAuthDocument
        fields = ( 'dateOfAdmission','dateOfPreAuth' , 'hospitalName' , 'hospitalCode' , 'justification',
                  'on_BedPhotograph' , 'admitCaseSheet' , 'labReport' , 'radiologyReport' )                


class PreAuthLinkCaseNumberSerialzier(serializers.ModelSerializer):
    class Meta:
        model = PreAuthLinkCaseNumber
        fields = '__all__'


class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField()


class ClaimFormSerializer(serializers.ModelSerializer):
    # Radiology =  serializers.ListField(child=serializers.FileField(allow_empty_file=True, use_url=False),write_only=True , required = False)
    class Meta:
        model =  ClaimManagement
        fields = ( 'CaseNumberID','CaseNumber','AdmitCase_ClinicalSheet' , 'ICP' , 'MedicationChart' ,'InitialSheet' ,
                     'TPRChart' , 'VitalChart' , 'LOS_StayChart' , 'CaseSheets_OtheDocuments' , 'Microbiology',
                     'Biochemistry' , 'Pathology' , 'SerologyInvestigation' , 'Radiology' ,'OT_ProcedureSheets',
                     'AnaesthesiaNotes' , 'dischargeDate' , 'DischargeType' , 'DischargeSummaryDocument' , 'MortalityAudit', 'DeathCertificate',
                      'BloodTransfusion' , 'BTSticker' , 'CrossMatchReport' , 'OtherDocuments' ,'Status' )


class DumpExcelSerializer(serializers.Serializer):
    excel_file = serializers.FileField(required=True)

    def validate(self, data):
        if data['excel_file'] == None or data['excel_file'] == "":
            raise ValidationError('excel_file can not be empty')
        
        return data
   