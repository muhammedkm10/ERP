from .serializer import UserSerializer,ServiceSerializer,Sub_ServiceSerializer,Expense_serilizer,ClientSerializer,Booking_serializer,Booked_Sub_Services_serializer,Client_requirements_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_token
from user_app.models import ShopOwners,Services,Sub_Services
from rest_framework import viewsets
from .models import Expenses,Bookings,Booked_Sub_Services,Clients,Client_requirements
# **********************************************************  API SECTION ********************************************



# Create your views here.
class Authentication(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")
        if not phone or not password:
            return Response({"error": "email and password are required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = ShopOwners.objects.get(phone = phone)
        except ShopOwners.DoesNotExist:
            return Response({"error": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)
        if  user.block:
            return Response({"error": "you are blocked."},
                            status=status.HTTP_401_UNAUTHORIZED)
        if not user.password != password:
            return Response({"error": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)
        # If password is correct, generate a token
        token = generate_token(user.id, phone)
        response_data = {'token': token}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def get(self,request):
        user_id = request.user_id
        queryset = ShopOwners.objects.get(id = user_id)
        serializer = UserSerializer(queryset,many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
############################################################# service management ################################################# 
    
class Services_management(APIView):
    def get(self,request):
        user_id = request.user_id
        queryset = Services.objects.filter(user_id = user_id)
        serializer = ServiceSerializer(queryset,many= True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
############################################################# sub service management #################################################     

class Sub_Services_management(APIView):
    def get(self,request,service_id):
        queryset = Sub_Services.objects.filter(service_name_id = service_id)
        serializer = Sub_ServiceSerializer(queryset,many= True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
   
   
################################################################ BOOKING MANAGEMENT  #############################################

class Booking_management(APIView):
    def get(self,request,booking_id = None):
        owner_id = request.user_id
        if booking_id:
            try:
               booking = Bookings.objects.get(id = booking_id)
            except:
                return Response({'error':'not exist'}, status=status.HTTP_400_BAD_REQUEST)
            serilizer = Booking_serializer(booking,many = False)
            sub_services = Booked_Sub_Services.objects.filter(booking_id = booking.id)
            serializer1 = Booked_Sub_Services_serializer(sub_services,many = True)
            Client_requirement = Client_requirements.objects.get(booking = booking)
            serializer2  = Client_requirements_serializer(Client_requirement,many = False)
            return Response({"Booking details":serilizer.data,"sub_service_details":serializer1.data,'client_requirements':serializer2.data},status=status.HTTP_200_OK)
        else:
            query_set = Bookings.objects.filter(owner_name_id = owner_id)
            serilizer = Booking_serializer(query_set,many = True)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        
        
    #  add booking
    def post(self,request):
        owner_id = request.user_id
        client_id = request.data.get("client_id")
        service_id  = request.data.get("service_id")
        start_date  = request.data.get("start_date")
        end_date  = request.data.get("end_date")
        start_time  = request.data.get("start_time")
        end_time  = request.data.get("end_time")
        total_amount  = request.data.get("total_amount")
        advance_amount  = request.data.get("advance_amount")
        sub_services = request.data.get('sub_services')
        description = request.data.get('description')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        img4 = request.FILES.get('img4')
        if sub_services is None:
            return Response({'error': "sub services are needed"}, status=status.HTTP_400_BAD_REQUEST) 
        try:
           
           booking = Bookings.objects.create(owner_name_id = owner_id,client_id_id = client_id,service_id_id = service_id,start_date = start_date,start_time = start_time,ending_time = end_time,end_date = end_date,total_amount = total_amount,advance_amount= advance_amount)
        except Exception as e:
            return Response({"add every fields correctly":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        for sub in sub_services:
            Booked_Sub_Services.objects.create(
                booking = booking,
                booked_sub_services_id = sub
            )
        Client_requirements.objects.create(
                booking=booking,
                description=description,
                img1=img1,
                img2=img2,
                img3=img3,
                img4=img4
            ) 
        return Response({'success':'booking created succesfully'},status=status.HTTP_200_OK)
       
        
        
        
class Add_client(APIView):
    def post(self,request):
        request.data['owner_name'] = request.user_id
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        owner_id = request.user_id
        query_set  = Clients.objects.filter(owner_name_id = owner_id)
        serializer = ClientSerializer(query_set,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
                
        
        
        
   
   
#########################################################   expense management  #########################################################33 
class ExpenseViewSet(APIView):
    def get(self,request,exp_id = None):
        owner_id = request.user_id
        if not exp_id:
           expenses = Expenses.objects.filter(owner_name = owner_id)
           serializer = Expense_serilizer(expenses , many = True)
        else:
            try:
              expenses = Expenses.objects.get(id = exp_id)
            except:
                return Response({"error": "no such expenses"},
                            status=status.HTTP_400_BAD_REQUEST)
            serializer = Expense_serilizer(expenses)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        owner_id = request.user_id
        date = request.data.get("date")
        expense = request.data.get("expense")
        type = request.data.get("type")
        description = request.data.get("description")
        
        request.data['owner_name'] = owner_id
        serializer = Expense_serilizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def patch(self,request,exp_id = None):
        owner_id = request.user_id
        date = request.data.get("date")
        expenses = request.data.get("expense")
        type = request.data.get("type")
        description = request.data.get("description")
        request.data['owner_name'] = owner_id
        print(exp_id,"id")
        try:
            expense = Expenses.objects.get(id = exp_id)
            expense.date  = date
            expense.type = type
            expense.date  = date
            expense.description = description
            expense.save()
            return Response({'success':'updated'},status=status.HTTP_201_CREATED)
        except:
           return Response({"error":"data is not present"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,exp_id = None):
        try:
            Expenses.objects.get(id = exp_id).delete()
            return Response({"success":'deleted successfully'},status=status.HTTP_200_OK)
            
        except:
            return Response({"error":'no data'},status=status.HTTP_400_BAD_REQUEST)
        
        


class Second_Authentication(APIView):
    def post(self, request):
        owner_id = request.user_id
        password = request.data.get("password")
        if  not password:
            return Response({"error": "password is required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = ShopOwners.objects.get(id  = owner_id,password  = password)
        except ShopOwners.DoesNotExist:
            return Response({"error": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)
        if not user.password != password:
            return Response({"error": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)
        # If password is correct, generate a token
        return Response({"message":'success'},status=status.HTTP_200_OK)