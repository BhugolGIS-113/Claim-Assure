from django.db import models
from PreAuth.models import *

# Create your models here.


class CaseSheet(models.Model):
    user = models.ForeignKey(User , related_name= "CaseSheet_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='CaseSheet_caseNumber', on_delete=models.CASCADE)
    # CaseNumber = models.CharField(max_length= 255 , blank = True , null = True)
    AdmitCase_ClinicalSheet =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    ICP =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    MedicationChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    InitialSheet =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    TPRChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    VitalChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    LOS_StayChart =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 
    OtherDocuments =  models.FileField(upload_to= 'ClaimDocuments/CaseSheet' , blank = True ,     null = True ) 


class LabTest(models.Model):
    user = models.ForeignKey(User , related_name= "LabTest_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='LabTest_caseNumber', on_delete=models.CASCADE)
    Microbiology = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True ) 
    Biochemistry =  models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True ) 
    Pathology = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True )
    SerologyInvestigation = models.FileField(upload_to= 'ClaimDocuments/Lab Test' , blank = True ,     null = True )
    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/Lab Test', blank = True , null = True )

class Reports(models.Model):
    user = models.ForeignKey(User , related_name= "Reports_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='Reports_caseNumber', on_delete=models.CASCADE)
    Radiology = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    OT_ProcedureSheets = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    AnaesthesiaNotes = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True ,     null = True )
    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/Reports' , blank = True , null = True )

class DischargeSummary(models.Model):
    user = models.ForeignKey(User , related_name= "DischargeSummary_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='DischargeSummary_caseNumber', on_delete=models.CASCADE)
    dischargeDate = models.DateTimeField()
    DischargeType = models.CharField(max_length=255 ) # drop down 
    DischargeSummaryDocument = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 
    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True , null = True )
    
class DeathSummary(models.Model):
    user = models.ForeignKey(User , related_name= "DeathSummary_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='DeathSummary_caseNumber', on_delete=models.CASCADE)
    MortalityAudit  = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 
    DeathCertificate = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True ,     null = True ) 
    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/Death Summary' , blank = True , null = True )



class BloodDocuments(models.Model):
    user = models.ForeignKey(User , related_name= "BloodDocuments_user" , on_delete=models.CASCADE)
    CaseNumberID = models.OneToOneField(PreAuthLinkCaseNumber , related_name='BloodDocuments_caseNumber', on_delete=models.CASCADE)
    BloodTransfusion = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 
    BTSticker = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 
    CrossMatchReport = models.FileField(upload_to= 'ClaimDocuments/Blood Documents' , blank = True ,     null = True ) 
    OtherDocuments = models.FileField(upload_to= 'ClaimDocuments/OtherDoc' , blank = True , null = True )
    
    # Status = models.CharField(max_length=255 )




class DumpExcel(models.Model):
    # user = models.ForeignKey(User , related_name="dumps_user" , on_delete= models.CASCADE)
    CaseNo = models.CharField(max_length=255 , primary_key= True )
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
    

class MPClaimPaidExcel(models.Model):
    CaseNumber = models.CharField(max_length=100, primary_key=True)
    WorkflowStatus	= models.CharField(max_length=255 , blank = True , null = True)
    StatusUpdateDate	 = models.CharField(max_length=255 , blank = True , null = True)
    NHPMID	= models.CharField(max_length=255 , blank = True , null = True)
    FamilyID	= models.CharField(max_length=255 , blank = True , null = True)
    PatientName	= models.CharField(max_length=255 , blank = True , null = True)
    Age	= models.IntegerField( )
    Gender	 = models.CharField(max_length=255 , blank = True , null = True)
    Patients_Home_District	= models.CharField(max_length=255 , blank = True , null = True)
    Patients_Home_State = models.CharField(max_length=255 , blank = True ,  null  = True)	
    Patient_Phone_No	= models.PositiveBigIntegerField( blank = True , null = True)
    Address	= models.TextField(max_length=255 , blank = True , null = True)
    Communication_Address	 = models.TextField(max_length=255 , blank = True)
    Communication_Contact_No =  models.CharField( max_length=255 ,blank = True , null = True)
    Communication_Village = 	models.CharField(max_length=255 , blank = True ,  null  = True)
    Communication_Mandal = models.CharField(max_length=255 , blank = True ,  null  = True) 	
    Communication_District	 = models.CharField(max_length=255 , blank = True ,  null  = True)
    Communication_State	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Speciality	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Patient_IP_OP	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Procedure_Code	 = models.CharField(max_length=255 , blank = True ,  null  = True)
    Procedure	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Procedure_Auto_Approve = models.CharField(max_length=255 , blank = True ,  null  = True)
    Medical_or_Surgery	= models.CharField(max_length=255 , blank = True ,  null  = True)
    IP_Registration_Date = models.CharField(max_length=255 , blank = True ,  null  = True)	
    Hospital_Name	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Admission_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_Initiation_Date = models.CharField(max_length=255 , blank = True ,  null  = True)	
    PreAuth_Initiation_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_Cancel_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_Approval_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_Approval_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_Rejection_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Enhancement_Flag	=  models.CharField(max_length=255 , blank = True ,  null  = True)
    Enhancement_Approved_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Surgery_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Discharge_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Death_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Raised_Date = models.CharField(max_length=255 , blank = True ,  null  = True)	
    Claim_Paid_Amount= models.CharField(max_length=255 , blank = True ,  null  = True)
    CPD_Approved_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    CPD_rejected_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    SHA_Approved_Date = models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Paid_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_UTR_Number	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Hospital_District	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Hospital_State	= models.CharField(max_length=255 , blank = True ,  null  = True)
    PreAuth_approval_remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    PreAuth_rejection_remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Claim_approval_remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Claim_rejection_remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Claim_Initiated_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    RF_Amount	=models.CharField(max_length=255 , blank = True ,  null  = True)
    TDS_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Amount_paid_to_Hospital	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Approved_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Updated_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Preauth_Pending_Remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Preauth_Pending_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Preauth_Pending_Updated_Remarks= models.TextField(max_length=255 , blank = True ,  null  = True)
    Preauth_Pending_Updated_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Pending_Remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Claim_Pending_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Claim_Pending_Updated_Remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Claim_Pending_Updated_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Last_Updated_User	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Is_Aadhar_Benificaiary = models.CharField(max_length=255 , blank = True ,  null  = True)	
    BioAuth_at_Registration  = models.CharField(max_length=255 , blank = True ,  null  = True)	
    BioAuth_at_Discharge = models.CharField(max_length=255 , blank = True ,  null  = True)
    Erroneous_Initiated_Amount = models.CharField(max_length=255 , blank = True ,  null  = True)	
    Erroneous_Initiated_Date = models.CharField(max_length=255 , blank = True ,  null  = True)
    Erroneous_Approved_Amount = models.CharField(max_length=255 , blank = True ,  null  = True)	
    Erroneous_Approved_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Erroneous_Paid_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Erroneous_UTR_Number	= models.CharField(max_length=255 , blank = True ,  null  = True)
    IP_Number	= models.CharField(max_length=255 , blank = True ,  null  = True)
    CPD_Pending_Count	= models.CharField(max_length=255 , blank = True ,  null  = True)
    CPD_Processing_Time	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Revoked_Case	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Revoked_Date	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Revoked_Remarks	= models.TextField(max_length=255 , blank = True ,  null  = True)
    Insurance_Liable_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Trust_Liable_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Patient_Liable_Amount	= models.CharField(max_length=255 , blank = True ,  null  = True)
    Actual_Registration_Date = models.CharField(max_length=255 , blank = True ,  null  = True)


    def __str__(self):
        return self.CaseNumber