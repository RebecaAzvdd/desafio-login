from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_users(request):
    users = User.objects.values('id', 'username', 'email')
    return Response(users)
