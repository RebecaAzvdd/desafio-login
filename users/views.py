from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'E-mail inexistente')
            return redirect('login')

        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Senha inválida')

    return render(request, 'users/login.html')

def registrar_view(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return redirect('registrar')

        if not validacao(senha):
            messages.error(request, "A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.")
            return redirect('registrar')

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return redirect('registrar')

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'users/registrar.html')

def menu_view(request):
    return render(request, 'users/menu.html')

def validacao(senha):
     return (len(senha) >= 8 and
            any(c.isupper() for c in senha) and
            any(c.isdigit() for c in senha) and
            any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/`~" for c in senha))
