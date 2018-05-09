from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from curriculo.models import User,Aluno,Professor
import random
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
import LMSbasico.settings

def index(request):
    return render(request,'index.html')

def cursos(request):
    return render(request,'cursos.html')

def detalhecurso(request):
    return render(request,'detalhecurso.html')

def detalhedisciplina(request):
    return render(request,'detalhedisciplina.html')

def disciplinascurso(request):
    return render(request,'disciplinascurso.html')

def matricula(request):
    return render(request,'matricula.html')

def novaDisciplina(request):
    return render(request,'novaDisciplina.html')

def novo_curso(request):
    return render(request,'novo_curso.html')


def NovoAluno(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoAluno.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            tipo = "A"
            Aluno.objects.create_user(username = username,password = password,name = name,email= email,celular = celular,tipo = tipo)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")

def NovoCoordenador(request):
    Usuario = request.user
    if Usuario.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoCoordenador.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            User.objects.create_user(username = username,password = password,name = name,email= email,celular = celular)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")

def NovoProfessor(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoProfessor.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            apelido = request.POST.get("apelido")
            Professor.objects.create_user(username = username,password = password,name = name,email= email,celular = celular,tipo = "P",apelido = apelido)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")


def recover(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        return render(request,'recover.html')



def teste_coordenador(user):
    return user.tipo == 'C'

def teste_aluno(user):
    return user.tipo == 'A'

def teste_professor(user):
    return user.tipo == 'P'


    
@login_required(login_url='/curriculo/login')
@user_passes_test(teste_coordenador,login_url='/curriculo/index',redirect_field_name=None)
def areaUser(request):
    return render(request,"areaUser.html")


@login_required(login_url='/curriculo/login')
@user_passes_test(teste_aluno,login_url='/curriculo/index',redirect_field_name=None)
def areaAluno(request):
    return render(request,"areaAluno.html")


@login_required(login_url='/curriculo/login')
@user_passes_test(teste_professor,login_url='/curriculo/index',redirect_field_name=None)
def areaProfessor(request):
    return render(request,"areaProfessor.html")


@login_required(login_url='/curriculo/index')
def first_edit_senha(request):
    if request.method == "GET":
        return render(request,"first_edit_senha.html")
    else:
        Usuario = request.user
        new_password = request.POST.get("novasenha")
        confirm_senha = request.POST.get("confirmsenha")
        if new_password == confirm_senha:
            Usuario.set_password(new_password)
            Usuario.save()
            return render(request,"index.html")
        else:
            return render(request,"first_edit_senha.html")




