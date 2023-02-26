from django.db import models
from django.core.exceptions import ValidationError
from Authentications.models import User
from django.utils.translation import gettext_lazy as _ 
# Create your models here.

def validate_length(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 12:
        raise ValidationError(f'{value} is above 12 digits')
    if length < 12:
        raise ValidationError(f'{value} is less than 12 digits')

def validate_number(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 10:
        raise ValidationError(f'{value}  is above 10 digits')
    if length < 10:
        raise ValidationError(f'{value}  is less than 10 digits')

   
class PersonalInfo(models.Model):
    user = models.ForeignKey( User , related_name= "user_profile" , on_delete= models.CASCADE)
    NHPMID = models.CharField(max_length=255 , blank = False , unique= True )
    nameOfPatient = models.CharField(max_length= 255 , blank = False , null = False)
    adharPhotograph = models.ImageField(upload_to= 'AdharCard_PhotoGraphs' , blank = True , null = True )
    adharNumber = models.PositiveBigIntegerField(validators=[validate_length] , blank = False , null = False , unique= True)
    DOB = models.DateField()
    gender = models.CharField(max_length=10 , blank = True , null = True )
    mobileNumber = models.PositiveBigIntegerField( validators=[validate_number] , blank = True , null = True)
    alternativeNumber =  models.PositiveBigIntegerField(validators=[validate_number] , blank = True , null = True)
    addressLine1 = models.CharField(max_length= 255 , blank = True , null = True )
    addressLine2 = models.CharField(max_length=  255 , blank= True , null = True)
    district = models.CharField(max_length = 50 , blank = True , null = True)
    pincode = models.IntegerField(blank = True , null = True )
    RationCardNumber = models.CharField(max_length=50 ,  blank = True , null = True )
    RationCardPhotograph = models.ImageField( upload_to= 'RationCard_Photographs'  , blank = True , null = True)

    def __str__(self):
        return "NHPMID - " + self.NHPMID

class PreAuthDocument(models.Model):
    user = models.ForeignKey(User , related_name= "Preauth_document" , on_delete=models.CASCADE)
    PersonalInfoID = models.ForeignKey(PersonalInfo , related_name="PreAuth_personal" ,on_delete=models.CASCADE)
    PreAuthID = models.CharField(max_length=255 ,unique=True)
    dateOfAdmission = models.DateTimeField()
    dateOfPreAuth = models.DateTimeField()
    hospitalName = models.CharField(max_length= 255 , blank = False , null = False)
    hospitalCode = models.CharField(max_length= 255 , blank = False , null = False)
    justification = models.FileField(upload_to='PreAuthDocuments/justification' , blank = True , null = True )
    on_BedPhotograph = models.FileField(upload_to= 'PreAuthDocuments/on_bedPhotograph' , blank = True ,     null = True )   
    admitCaseSheet = models.FileField(upload_to= 'PreAuthDocuments/admitCaseSheet' ,  blank = True , null = True )
    labReport = models.FileField(upload_to= 'PreAuthDocuments/labReport' , blank = True , null = True)
    radiologyReport = models.FileField(upload_to= 'PreAuthDocuments/radiologyReport' , blank = True , null = True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.PreAuthID

class PreAuthLinkCaseNumber(models.Model):
    user = models.ForeignKey(User ,  related_name= "PreAuthLinkCaseNumber_user" ,on_delete= models.CASCADE)
    PreAuthID = models.OneToOneField(PreAuthDocument , related_name= "PreAuth_PreAuthID" , on_delete=models.CASCADE )
    CaseNumber = models.CharField(max_length=100 , blank = True , null = True)

    def __str__(self):
        return self.CaseNumber



class ClaimManagement(models.Model):
    user = models.ForeignKey(User , related_name= "ClaimManagement_user" , on_delete=models.CASCADE)
    CaseNumberID = models.ForeignKey(PreAuthLinkCaseNumber , related_name='PreAuthLinkCaseNumber_caseNumber', on_delete=models.CASCADE)
    CaseNumber = models.CharField(max_length= 255 , blank = True , null = True)
    AdmitCase_ClinicalSheet =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    ICP =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    MedicationChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    InitialSheet =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    TPRChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    VitalChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    LOS_StayChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    CaseSheets_OtheDocuments =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 

    Microbiology = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True ) 
    Biochemistry =  models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True ) 
    Pathology = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True )
    SerologyInvestigation = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True )
    
    Radiology = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    OT_ProcedureSheets = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    AnaesthesiaNotes = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    
    dischargeDate = models.DateTimeField()
    DischargeType = models.CharField(max_length=255 ) # drop down 
    DischargeSummaryDocument = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 
    MortalityAudit  = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 
    DeathCertificate = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 

    BloodTransfusion = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 
    BTSticker = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 
    CrossMatchReport = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 

    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/OtherDoc' , blank = True , null = True )
    Status = models.CharField(max_length=255 )

    def __str__(self):
        return self.CaseNumber


from django.utils import timezone

class DumpExcel(models.Model):
    # user = models.ForeignKey(User , related_name="dumps_user" , on_delete= models.CASCADE)
    CaseNo = models.CharField(max_length=255 , blank = True , null = True)
    ClaimNo = models.CharField(max_length=255 , blank = True , null = True)
    RegistrationNumber = models.CharField(max_length=255 , blank = True , null = True)
    NHPMId = models.CharField(max_length=255 , blank = True , null = True)
    FamilyId = models.CharField(max_length=255 , blank = True , null = True)
    PatientDistrict = models.CharField(max_length=255 , blank = True , null = True)
    Gender = models.CharField(max_length=255 , blank = True , null = True)
    Age = models.IntegerField( )
    CategoryDetails = models.CharField(max_length=255 , blank = True , null = True)
    ProcedureDetails = models.TextField(max_length=255 , blank = True , null = True)
    CaseType = models.CharField(max_length=255 , blank = True , null = True)
    CaseStatus = models.CharField(max_length=255 , blank = True , null = True)
    HospitalName = models.CharField(max_length=255 , blank = True , null = True)
    HospitalCode = models.CharField(max_length=255 , blank = True , null = True)
    HospitalDistrict = models.CharField(max_length=255 , blank = True , null = True)
    PreauthAmount =models.CharField(max_length=255, blank= True , null = True)
    ClaimInitaiatedAmount = models.CharField(max_length=255, blank= True , null = True)
    CPDApprovedAmount = models.CharField(max_length=255, blank= True , null = True)
    ClaimApprovedAmount = models.CharField(max_length=255 , blank = True , null = True)
    AssignedFlag = models.CharField(max_length=255 , blank = True , null = True)
    AssignedUser = models.CharField(max_length=255 , blank = True , null = True)
    AssignedGroup = models.CharField(max_length=255 , blank = True , null = True)
    IPNumber = models.CharField(max_length=255, blank= True , null = True)
    PreauthApprovedAmount = models.CharField(max_length=255, blank= True , null = True)

    IPRegistrationDate = models.CharField(max_length=255, blank= True , null = True)
    PreauthApproveDate =  models.CharField(max_length=255, blank= True , null = True)
    PreauthRejectedDate = models.CharField(max_length=255, blank= True , null = True)
    SurgeryDate =models.CharField(max_length=255, blank= True , null = True)
    DeathDate =models.CharField(max_length=255, blank= True , null = True)
    DischargeDate = models.CharField(max_length=255, blank= True , null = True)
    ClaimSubmittedDate = models.CharField(max_length=255, blank= True , null = True)
    ActualClaimSubmittedDate =models.CharField(max_length=255, blank= True , null = True)
    AdmissionDate = models.CharField(max_length=255, blank= True , null = True)
    PreauthDate = models.CharField(max_length=255, blank= True , null = True)
    ActualRegistrationDate = models.CharField(max_length=255, blank= True , null = True)

    def __str__(self):
        return self.CaseNo

    # def save(self, *args, **kwargs):
        # self.IPRegistrationDate = timezone.datetime.strptime(self.IPRegistrationDate   , '%d/%m/%Y')
    #     self.PreauthApproveDate = timezone.datetime.strptime(self.PreauthApproveDate, '%d/%m/%Y %H:%M:%S %p')
    #     # self.PreauthRejectedDate = timezone.datetime.strptime(self.PreauthRejectedDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.SurgeryDate = timezone.datetime.strptime(self.SurgeryDate, '%d/%m/%Y %H:%M:%S %p')

    #     self.DeathDate = timezone.datetime.strptime(self.DeathDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.DischargeDate = timezone.datetime.strptime(self.DischargeDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.ClaimSubmittedDate = timezone.datetime.strptime(self.ClaimSubmittedDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.ActualClaimSubmittedDate = timezone.datetime.strptime(self.ActualClaimSubmittedDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.AdmissionDate = timezone.datetime.strptime(self.AdmissionDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.PreauthDate = timezone.datetime.strptime(self.PreauthDate, '%d/%m/%Y %H:%M:%S %p')
    #     self.ActualRegistrationDate = timezone.datetime.strptime(self.ActualRegistrationDate, '%d/%m/%Y %H:%M:%S %p')
        
    #     super(DumpExcel, self).save(*args, **kwargs)


