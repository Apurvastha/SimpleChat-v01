from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('chat/<int:receiver_id>/', views.chat_room, name='chat_room'),
    path('send-message/', views.send_message, name='send_message'),
    path('get-messages/<int:receiver_id>/', views.get_messages, name='get_messages'),
]
