from django.urls import path,include
from .views import Authentication,Services_management,Sub_Services_management,ExpenseViewSet,Booking_management,Add_client,Second_Authentication
from rest_framework.routers import DefaultRouter




urlpatterns = [
    
    ################################################ API END POINTS ###################################################
    # basic management and login
    path("user_login",Authentication.as_view()),
    path("service_management",Services_management.as_view()),
    path("sub_service_management/<str:service_id>",Sub_Services_management.as_view()),
    
    # booking management
    
    path('booking_management',Booking_management.as_view()),
    path('booking_management/<str:booking_id>',Booking_management.as_view()),
    
    
    
    # add clients
    path("client_management", Add_client.as_view(),),
    
    # reauthentication
    path("re_auth", Second_Authentication.as_view(),),

    
    
    # expense management
    path("expense_management",ExpenseViewSet.as_view()),
    path("expense_management/<str:exp_id>",ExpenseViewSet.as_view())
    
    
    
    
    
]

