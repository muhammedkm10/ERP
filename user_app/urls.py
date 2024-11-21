from django.urls import path
from . views import Client_login,Admin_home,Logout,Add_user,Edit_user,Delete_user,Block_user,Unblock_user,Search_user,Show_services,Add_services,Edit_service,Delete_service,Add_sub_services,Edit_sub_service,Delete_sub_service,Show_sub_services

urlpatterns = [
    # user management
    
    path('',Client_login ,name ="client_login"),
    path('admin_home',Admin_home ,name ="admin_home"),
    path('add_user',Add_user ,name ="add_user"),
    path('edit_user/<str:id>',Edit_user ,name ="edit_user"),
    path('delete_user/<str:id>',Delete_user ,name ="delete_user"),
    path('block_user/<str:id>',Block_user ,name ="block_user"),
    path('unblock_user/<str:id>',Unblock_user ,name ="unblock_user"),
    path('search',Search_user ,name ="search"),
    
    
    # service management
    path('add_services/<str:user_id>',Add_services,name ="add_services"),
    path('edit_service/<str:user_id>/<str:service_id>',Edit_service,name ="edit_services"),
    path('delete_service/<str:user_id>/<str:service_id>',Delete_service,name ="delete_services"),
    path('showservices/<str:user_id>',Show_services ,name ="show_services"),
    
    
        
    # sub service management
    path('add_sub_services/<str:service_id>',Add_sub_services,name ="add_sub_services"),
    path('edit_sub_service/<str:service_id>/<str:subservice_id>',Edit_sub_service,name ="edit_sub_services"),
    path('delete_sub_service/<str:service_id>/<str:subservice_id>',Delete_sub_service,name ="delete_sub_services"),
    path('show_sub_services/<str:service_id>',Show_sub_services ,name ="show_sub_services"),
    
    path('logout',Logout ,name ="logout")
    
    
]

