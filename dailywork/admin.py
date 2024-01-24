from django.contrib import admin
from . models import user_infor
from . models import tickets_info
from . models import user_events_info



admin.site.register(user_infor)
admin.site.register(user_events_info)
admin.site.register(tickets_info)