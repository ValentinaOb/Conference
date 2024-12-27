from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt

# Create your views here.
@login_required

def home(request):
    return HttpResponse("All")
    return render(request, 'home.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.Post or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request,"authentication/registr.html",{"form" : form})


def signup(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name', False)
        email = request.POST.get('email', False)
        pswd = request.POST.get('pswd', False)

        myuser=User.objects.create_user(user_name, email, pswd)
        myuser.save()

        messages.success(request,"Successful")
        
        return redirect('home')
        #return HttpResponseRedirect("")
    return render(request,"authentication/registr.html")

    
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        pswd = request.POST['pswd']

        user=authenticate(request,email=email, pswd=pswd)

        if user is not None:
            login(request,user)
            return redirect('home')
        #return render(request, "../index.html",)    
        else:
            messages.error(request, "Invalid login credentials")
        
    return render(request,"authentication/registr.html")
        

def signin(request):
    pass