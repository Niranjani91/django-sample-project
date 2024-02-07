
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from dailywork.models import user_infor
from dailywork.models import user_events_info
from dailywork.models import admin_info
from dailywork.models import tickets_info


from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout

from chaseyourdreams.serializers import UserInfoSerializer
from chaseyourdreams.serializers import UserEventsInfoSerializer
from chaseyourdreams.serializers import AdminInfoSerializer
from chaseyourdreams.serializers import TicketInfoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import time
from django.shortcuts import redirect
from django.urls import reverse
from calendar import HTMLCalendar
import datetime

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


@csrf_exempt
def register(request):
    return render(request,"./actual_register.html")
    

def admin_log_out(request):
    logout(request)
    return redirect('index')



def registered(request):
    template = loader.get_template('registered.html')
    return HttpResponse(template.render())

def admin(request):
    return render(request,"admin.html")

def users_list(request):
    return render(request,"users_list.html")

def tickets_list(request):
    return render(request,"tickets_list.html")

def user_logout_page(request,main_user_name):
    logout(request)
    return redirect('index')

def login(request):
    if request.method == 'POST':
        user_name_ = request.POST.get("user_name")
        password = request.POST.get("pass_word")
        user_exists = user_infor.objects.filter(username=user_name_).values("username","password")
        user_exists = list(user_exists)
        print(user_exists)
        if len(user_exists)==0:
            print("no such user exists")
            messages.error(request,"no such user exists")
        else:
            if user_exists[0]["username"] == user_name_ and user_exists[0]["password"] == password:
                print("login successful")
                redirect_to_user="../"+user_name_+"/"
                return redirect(redirect_to_user)
            else:
                print("incorrect password")
                messages.error(request,"incorrect password")
    return render(request,"./login.html")


                

@api_view(['GET' , 'POST'])
def admin_info_list(request):
    if request.method == 'GET':
        all_admins = admin_info.objects.all()
        serializer = AdminInfoSerializer(all_users, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST':
        serializer = AdminInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    return Response({"key":"value"},status=status.HTTP_200_OK)


@api_view(['GET' , 'PUT' , 'DELETE'])
def admin_details(request, admin_name):

    try:
        admin__name = admin_info.objects.get(pk=admin_name)
    except admin_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminInfoSerializer(admin__name)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = AdminInfoSerializer(admin__name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        admin_info.delete(admin__name)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET' , 'POST'])
def ticket_info_list(request):
    if request.method == 'GET':
        all_tickets = tickets_info.objects.all()
        serializer = TicketInfoSerializer(all_tickets, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST':
        serializer = TicketInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    return Response({"key":"value"},status=status.HTTP_200_OK)



@api_view(['GET' , 'PUT', 'DELETE'])
def ticket_details(request,main_user_name,main_ticket_title,main_ticket_status):
    if request.method == 'DELETE':
        tickets_info.objects.filter(username=main_user_name,ticket_title=main_ticket_title,ticket_status=main_ticket_status).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET' , 'POST'])
def user_info_list(request):
    if request.method == 'GET':
        all_users = user_infor.objects.all()
        serializer = UserInfoSerializer(all_users, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    return Response({"key":"value"},status=status.HTTP_200_OK)




@api_view(['GET' , 'POST'])
def get_whole_events(request,main_user_name,event_date):
    if request.method == 'GET':
        all_events = user_events_info.objects.filter(username=main_user_name,event_date=event_date)
        serializer = UserEventsInfoSerializer(all_events,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        serializer = UserEventsInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    return Response({"key":"value"},status=status.HTTP_200_OK)



@api_view(['GET' , 'PUT' , 'DELETE'])
def events_details_info(request, main_user_name, event_date, event_title):

    if request.method == 'GET':
        all_events = user_events_info.objects.filter(username=main_user_name,event_date=event_date,event_title=event_title)
        serializer = UserEventsInfoSerializer(all_events,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'PUT':
        try:
            event = user_events_info.objects.filter(username=main_user_name,event_date=event_date,event_title=event_title)
            if len(event)>0:
                event=user_events_info.objects.get(pk=event[0].id)
            else:
                raise user_events_info.DoesNotExist
        except user_events_info.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserEventsInfoSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user_events_info.objects.filter(username=main_user_name,event_date=event_date,event_title=event_title).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET' , 'PUT' , 'DELETE'])
def user_details(request, username):

    try:
        user_username = user_infor.objects.get(pk=username)
    except user_infor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserInfoSerializer(user_username)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserInfoSerializer(user_username, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        user_infor.delete(user_username)
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def insert_into_user_info_model(request):
    username = request.GET.get("username")
    emailid = request.GET.get("emailid")
    password = request.GET.get("password")
    confirmpassword = request.GET.get("confirm_password")  
    firstname = request.GET.get("first_name") 
    middlename = request.GET.get("middle_name") 
    lastname = request.GET.get("last_name")
    pincode = request.GET.get('pin_code')
    nation = request.GET.get("nation")
    address = request.GET.get("address")
    return render(request,"user_home.html",{'user_name':username})

def user_login_page(request,main_user_name):
    return render(request,"main_user_login_page.html",{'user_name':main_user_name})

def user_profile_page(request,main_user_name):
    return render(request,"user_profile_page.html",{"user_name":main_user_name})

def user_ticket_page(request,main_user_name):
    return render(request,"user_ticket_page.html",{"user_name":main_user_name})

def user_timetable_page(request,main_user_name):
    return render(request,"timetable.html",{"user_name":main_user_name})

@api_view(['GET'])
def user_ticket_info_list(request,main_user_name):
    if request.method == "GET":
        all_tickets = tickets_info.objects.filter(username=main_user_name)
        serializer = TicketInfoSerializer(all_tickets,many=True)
        return JsonResponse(serializer.data,safe=False)

