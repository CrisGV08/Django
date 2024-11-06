from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    template_view = "index.html"
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, '⚠️Usuario inactivo, verifica tu correo para activar la cuenta⚠️')
                return redirect('index')
        else:
            try:
                existing_user = User.objects.get(username=username)
                if existing_user.is_active:
                    messages.error(request, 'Usuario o contraseña inválidos ⚠️')
                else:
                    messages.error(request, 'Usuario inactivo, verifica tu correo para activar la cuenta ⚠️')
            except User.DoesNotExist:
                messages.error(request, 'Usuario o contraseña inválidos ⚠️')
                
            return render(request, template_name=template_view)
    
    return render(request, template_name=template_view)



def register_view(request):
    template_view = "register.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Las contraseñas no coinciden ⚠️')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, ' ⚠️ El usuario ya existe ⚠️')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ El correo electrónico ya está registrado ⚠️')
            return redirect('register')

        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_active = False  
        user.save()
        
        messages.success(request, 'Registro exitoso. Verifica tu correo para activar la cuenta.')
        return redirect('register')
        
    return render(request, template_name=template_view)

def forgot_login_view(request):
    template_view = "forgot_password.html"
    return render(request, template_name=template_view)

def logout_view(request):
    logout(request)
    return redirect('index')
