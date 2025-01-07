from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt

def base(request):
    context={}
    return render(request, 'base/index.html', context)

def about(request):
    context={}
    return render(request, 'base/about-us.html', context)

def contact(request):
    context={}
    return render(request, 'base/contact.html', context)

def schedule(request):
    context={}
    return render(request, 'base/schedule.html', context)

def speaker(request):
    context={}
    return render(request, 'base/speaker.html', context)

def sign(request):
    context={}
    if request.method == "POST":
        user_name = request.POST.get("user_name", False) 
        email = request.POST.get('email', False)
        pswd = request.POST.get('pswd', False)
        
        if user_name:
            if User.objects.filter(user_name=user_name).exists():
                messages.success(request,"The User exists")
            else:
                user=User.objects.create_user(user_name, email, pswd)
                user.save()
                messages.success(request,"Successful")
                return redirect('home/')  
            
        else:
            user=authenticate(request,email=email, pswd=pswd)

            if user is not None:
                login(request,user)
                return redirect('home/')  
            else:
                messages.error(request, "Invalid login credentials")     
            
    return render(request, 'base/sign.html', context)