from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    template_view = "index.html"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name=template_view, context={'error': 'Credenciales inválidas'})
    return render(request, template_name=template_view)

def register_view(request):
    template_view = "register.html"
    return render(request, template_name=template_view)

def forgot_login_view(request):
    template_view = "forgot_login.html"
    return render(request, template_name=template_view)

