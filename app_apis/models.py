from django.db import models
from user_app.models import ShopOwners,Sub_Services,Services

# Create your models here.

class Expenses(models.Model):
    owner_name = models.ForeignKey(ShopOwners,on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)
    expense = models.IntegerField(null = False,blank = False)
    type = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    
class Clients(models.Model):
    owner_name =models.ForeignKey(ShopOwners, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50,null=False,blank=False)
    client_phone_1 = models.BigIntegerField(null=False,blank=False)
    client_phone_2 = models.BigIntegerField(null=True,blank=True)
    client_address  = models.TextField(null=False,blank=False)
    
class Bookings(models.Model):
    owner_name = models.ForeignKey(ShopOwners,related_name='owner_details',on_delete=models.CASCADE,null=False,blank=False)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE,related_name="service_details",null=False,blank=False)
    client_id = models.ForeignKey(Clients,on_delete=models.CASCADE,related_name='client_details',null=False,blank=False)
    start_date = models.DateField(null=False,blank=False)
    end_date = models.DateField(null=True,blank=True)
    total_amount = models.IntegerField(null = False,blank = False)
    advance_amount = models.IntegerField(null = False,blank = False)
    start_time = models.TimeField(null=True,blank=True)
    ending_time = models.TimeField(null=True,blank=True)
    
    
class Booked_Sub_Services(models.Model):
    booking = models.ForeignKey(Bookings,related_name='booking', on_delete=models.CASCADE)
    booked_sub_services = models.ForeignKey(Sub_Services,on_delete=models.CASCADE,related_name='client_details')
    
    
class Client_requirements(models.Model):
    booking = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    img1 = models.FileField(upload_to='uploads/',null=True,blank=True)
    img2 = models.FileField(upload_to='uploads/',null=True,blank=True)
    img3 = models.FileField(upload_to='uploads/',null=True,blank=True)
    img4 = models.FileField(upload_to='uploads/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    
    
    
    
    