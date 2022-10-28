from django.urls import path
from todolist.views import  add_todolist, show_todolist, register, login_user, logout_user, show_json, add_todoajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', add_todolist, name='add_todolist'),
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('add/', add_todoajax, name='add_todoajax'),
]