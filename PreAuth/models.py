from django.db import models
from django.core.exceptions import ValidationError
from Authentications.models import User
from django.utils.translation import gettext_lazy as _ 
from ClaimAssurance import settings
import os
from rest_framework import request
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


class PreAuthEnhancement(models.Model):
    user = models.ForeignKey(User , related_name = 'PreAuthEnhancement_User' , on_delete = models.CASCADE)
    PreAuthID = models.ForeignKey(PreAuthDocument , related_name = 'PreAuthEnhancement_PreAuthDocument' , on_delete = models.CASCADE)
    query = models.CharField(max_length = 255 , blank = True , null = True)
    documents = models.FileField(upload_to = 'PreAuthDocuments/Enhancement_Documents' , blank = True , null = True)


class ShapeFiles(models.Model):
    user = models.ForeignKey(User, related_name='shape_files', on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.folder_name

