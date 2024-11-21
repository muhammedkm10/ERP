from rest_framework.serializers import ModelSerializer
from user_app.models import ShopOwners,Services,Sub_Services
from .models import Expenses,Bookings,Clients,Booked_Sub_Services,Client_requirements



class UserSerializer(ModelSerializer):
    class Meta:
        model = ShopOwners
        fields = '__all__'
        
        
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        
class Sub_ServiceSerializer(ModelSerializer):
    class Meta:
        model = Sub_Services
        fields = '__all__'
        
class Expense_serilizer(ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'
        
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
    
class Booking_serializer(ModelSerializer):
    service_id = ServiceSerializer()
    client_id = ClientSerializer()
    class Meta:
        model = Bookings
        fields  = "__all__"
        
        
        
class Booked_Sub_Services_serializer(ModelSerializer):
    booked_sub_services = Sub_ServiceSerializer()
    class Meta:
        model = Booked_Sub_Services
        fields = '__all__'



class Client_requirements_serializer(ModelSerializer):
    class Meta:
        model  = Client_requirements
        fields = '__all__'