from rest_framework import serializers
from dailywork.models import user_infor
from dailywork.models import user_events_info
from dailywork.models import admin_info
from dailywork.models import tickets_info

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_infor
        fields = ['username','email_id','password','first_name','middle_name','last_name','pin_code','nation','address']

class UserEventsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_events_info 
        fields = ['event_title','event_description','event_comments','event_date','event_completed','username']

class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_info
        fields = ['admin_name','first_name','middle_name','last_name','pin_code','nation','address','email_id','password','admin_auth_pass']

class TicketInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets_info
        fields = ['username','ticket_title','ticket_description','ticket_status']