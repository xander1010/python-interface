from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.
def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['user'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')

def NewPage(request):
    return render_to_response('index.html')