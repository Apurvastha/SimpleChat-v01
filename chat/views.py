# chat/views.py
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q 
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Message


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_list')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    
    for user in users:
        # counting the messages between current user and rest of the users
        count = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=user)) |
            (Q(sender=user) & Q(receiver=request.user))
        ).count()
        # Add the count as an attribute to the user object
        user.msg_count = count
    
    return render(request, 'chat/user_list.html', {'users': users})

@login_required
def chat_room(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    return render(request, 'chat/chat_room.html', {
        'receiver': receiver     
     })
    

@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        receiver = User.objects.get(id=data['receiver_id'])
        # print(data['receiver'])
        # print(request.user)
        message = Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=data['content']
        )
        # print(message.id)
        return JsonResponse({
            'status': 'success',
            'message_id': message.id,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M')
        })
    else:
        return JsonResponse({'status': 'error'}, status=400)

@login_required
def get_messages(request, receiver_id):
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver_id=receiver_id)) |
        (Q(sender_id=receiver_id) & Q(receiver=request.user))
    ).order_by('timestamp')
    
    messages_data = [{
        'id': msg.id,
        'content': msg.content,
        'sender_id': msg.sender_id,
        'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M'),
    
    } for msg in messages]
    
    return JsonResponse({'messages': messages_data})