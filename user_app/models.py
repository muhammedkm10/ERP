from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



    
    
class ShopOwners(models.Model):
    phone = models.CharField(max_length=15, null=False, blank=False,unique=True)
    owner_name = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200,null=False,blank=False)
    email = models.EmailField(unique=False,null=False,blank=False)
    shop_name = models.CharField(max_length=200, null=False, blank=False)
    shop_phone = models.CharField(max_length=15, null=False, blank=False) 
    shop_address = models.TextField(null=False, blank=False)
    block = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['phone', 'owner_name', 'password']

    def clean(self):
        super().clean()  # Call the base class clean method to ensure other fields are cleaned
        if not self.phone.isdigit():
                raise ValidationError('Phone number must contain only digits.')
        if self.phone and len(self.phone) != 10:
            raise ValidationError('Phone number must be at least 10 digits long.')

    
    
    
class Services(models.Model):
    user = models.ForeignKey(ShopOwners,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200,null=False,unique=False)
    description = models.TextField()
    
    def __str__(self):
        return self.service_name
    
class Sub_Services(models.Model):
    service_name = models.ForeignKey(Services,on_delete=models.CASCADE)
    sub_service_name = models.CharField(max_length=200,null=False,unique=False)
    description = models.TextField()
    
    def __str__(self):
        return self.sub_service_name
    
    

