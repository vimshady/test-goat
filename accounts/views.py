from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user)
    return HttpResponse('OK')