from django.shortcuts import render

# Create your views here.

def register(request):
    # registered = False

    # if request.method = 'POST':
    return render(request,'user/register.html')


def login(request):
    return render(request,'user/login.html')
