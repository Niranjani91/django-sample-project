from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.index, name='home'),
    path('admin/',views.admin,name='admin'),
    path('users/',views.user_info_list,name='users'),
    path('users/<str:username>',views.user_details),
    path('register/user_home/',views.insert_into_user_info_model,name="user_home"),
    path('register/registered/',views.registered,name="registered"),
    path('<str:main_user_name>/',views.user_login_page,name="user_login_page"),
    path('<str:main_user_name>/profile/',views.user_profile_page,name="user_profile_page"),
    path('<str:main_user_name>/help/',views.user_ticket_page,name="user_ticket_page"),
    path('<str:main_user_name>/timetable/',views.user_timetable_page,name="user_timetable_page"),
    path('admin/users_list',views.users_list,name="users_list"),
    path('<str:main_user_name>/timetable/<str:event_date>',views.get_whole_events,name="get_whole_events"),
    path('<str:main_user_name>/timetable/<str:event_date>/<str:event_title>',views.events_details_info,name="put_delete_get"),
    path('tickets',views.ticket_info_list,name="tickets"),
    path('admin/tickets_list',views.tickets_list,name="tickets_list"),
    path('tickets/<str:main_user_name>&<str:main_ticket_title>&<str:main_ticket_status>',views.ticket_details)
]