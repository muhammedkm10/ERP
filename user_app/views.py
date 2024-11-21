from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import ShopOwners,Services,Sub_Services
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q


    

#*********************************************************   OTHER VIEWS *************************************************

# landing page
@never_cache
def Landing(request):
    return render(request,'landing_page.html')



# #####################################################  AUTHENTICATION  #####################################################
@never_cache
def Client_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    if request.method == 'POST':
        username = request.POST.get('client_name')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password,is_superuser = True)
        if user is not None:
            login(request,user)
            return redirect('admin_home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("client_login")
    return render(request,'admin_login.html')

@never_cache
@login_required
def Admin_home(request):
    qeuryset = ShopOwners.objects.all().order_by("-id")
    context = {
        "users" : qeuryset
    }
    return render(request,'admin_home.html',context)



@never_cache
def Logout(request):
    logout(request)
    request.session.pop('phone_number', None) 
    return redirect('client_login')


# ##############################################   USER MANAGEMENT #############################3
@login_required
def Add_user(request):
    owner_name = request.POST.get('owner_name')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    email = request.POST.get('email')
    shop_name = request.POST.get('shop_name')
    shop_phone = request.POST.get('shop_phone')
    shop_address = request.POST.get('shop_address')
    if shop_phone and len(shop_phone) != 10:
        messages.error(request, "Shop number should contains 10 digits")
        return redirect('admin_home')
    if len(phone) != 10 :
        messages.error(request, "Phone number should contains 10 digits")
        return redirect('admin_home')
    if password2 != password:
        messages.error(request, "The passeword should be same")
        return redirect('admin_home')
    try:
        ShopOwners.objects.create( 
        owner_name = owner_name,
        phone = phone,
        password = password,
        email = email,
        shop_name = shop_name,
        shop_phone = shop_phone,
        shop_address = shop_address,
        )
    except:
        messages.error(request, "Phone number is already present")
        return redirect('admin_home')
    messages.success(request, "User added succesfully")
    return redirect('admin_home')


@login_required
def Edit_user(request,id):
    user = ShopOwners.objects.get(id = id)
    owner_name = request.POST.get('owner_name')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    email = request.POST.get('email')
    shop_name = request.POST.get('shop_name')
    shop_phone = request.POST.get('shop_phone')
    shop_address = request.POST.get('shop_address')
    if shop_phone and len(shop_phone) != 10:
        messages.error(request, "Shop number should contains 10 digits")
        return redirect('admin_home')
    if len(phone) != 10 :
        messages.error(request, "Phone number should contains 10 digits")
        return redirect('admin_home')
    if len(password) == 0:
        messages.error(request, "The passeword should be same")
        return redirect('admin_home')
    try:
        user.owner_name = owner_name
        user.phone = phone
        user.password = password
        user.email = email
        user.shop_name = shop_name
        user.shop_phone = shop_phone
        user.shop_address = shop_address
        user.save()
    except:
        messages.error(request, "Phone number is already present")
        return redirect('admin_home')
    messages.success(request, "User updated succesfully")
    return redirect('admin_home')
    
@login_required
def Delete_user(request,id):
    ShopOwners.objects.get(id = id).delete()
    messages.success(request, "User deleted succesfully")
    return redirect('admin_home')

@login_required
def Block_user(request,id):
    user = ShopOwners.objects.get(id = id)
    user.block = True
    user.save()
    return redirect('admin_home')
    
@login_required
def Unblock_user(request,id):
    user = ShopOwners.objects.get(id = id)
    user.block = False
    user.save()
    return redirect('admin_home')

@login_required
@never_cache
def Search_user(request):
    search_term = request.GET.get('search', '') 
    if search_term:
        results = ShopOwners.objects.filter(Q(owner_name__icontains=search_term)|Q(phone =search_term)) 
    else:
        results = ShopOwners.objects.all() 

    return render(request, 'admin_home.html', {'users': results})




##############################         SERVICES CRUD OPERATIONS    #################################333

@login_required
@never_cache
def Show_services(request,user_id):
    queryset = Services.objects.filter(user__id = user_id).order_by("-id")
    context = {
        "user_id":user_id,
        'data':queryset
    }
    return render(request,'services.html',context)

@login_required
@never_cache
def Add_services(request,user_id):
    if request.method == 'POST':
        user = ShopOwners.objects.get(id = user_id)
        service_name = request.POST.get('service_name')
        description = request.POST.get('description')
        Services.objects.create(user = user,service_name = service_name,description = description)
        messages.success(request, "Service added succesfully")
        return redirect("show_services",user_id)

@login_required
@never_cache
def Edit_service(request,user_id,service_id):
    print(user_id,service_id,"in edit user")
    service_name = request.POST.get('service_name')
    description = request.POST.get('description')
    service = Services.objects.get(id = service_id)
    service.service_name = service_name
    service.description = description
    service.save()
    messages.success(request, "Service Updated succesfully")
    return redirect("show_services",user_id)
    
    
@login_required
@never_cache
def Delete_service(request,user_id,service_id):
    Services.objects.get(id = service_id).delete()   
    messages.success(request, "Service deleted succesfully") 
    return redirect("show_services",user_id)
    



############################################# CRUD  SUB SERVICES #############################################


@login_required
@never_cache
def Show_sub_services(request,service_id):
    print(service_id,"this is my service id")
    queryset = Sub_Services.objects.filter(service_name_id = service_id).order_by("-id")
    print(queryset)
    context = {
        "service_id":service_id,
        'data':queryset
    }
    return render(request,'sub_service.html',context)

@login_required
@never_cache
def Add_sub_services(request,service_id):
    if request.method == 'POST':
        service = Services.objects.get(id = service_id)
        sub_service_name = request.POST.get('sub_service_name')
        description = request.POST.get('description')
        Sub_Services.objects.create(service_name = service,sub_service_name = sub_service_name,description = description)
        messages.success(request, "sub Service added succesfully")
        return redirect("show_sub_services",service_id)

@login_required
@never_cache
def Edit_sub_service(request,service_id,subservice_id):
    sub_service_name = request.POST.get('sub_service_name')
    description = request.POST.get('description')
    sub_service = Sub_Services.objects.get(id = subservice_id)
    sub_service.sub_service_name = sub_service_name
    sub_service.description = description
    sub_service.save()
    messages.success(request, "sub Service Updated succesfully")
    return redirect("show_sub_services",service_id)
    
    
@login_required
@never_cache
def Delete_sub_service(request,service_id,subservice_id):
    Sub_Services.objects.get(id = subservice_id).delete()   
    messages.success(request, "Sub service deleted succesfully") 
    return redirect("show_sub_services",service_id)
    



# #####################################################    BOOKING SECTION  ################################################
    


    