from django.db import models
from PreAuth.models import *

# Create your models here.


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