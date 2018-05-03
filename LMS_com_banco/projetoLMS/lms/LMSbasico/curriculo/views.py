from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from curriculo.models import User,Aluno,Professor
import random

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
        return render(request,"index.html")

def NovoCoordenador(request):
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
        return render(request,"index.html")

def NovoProfessor(request):
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
        return render(request,"index.html")

        
def recover(request):
    return render(request,'recover.html')
