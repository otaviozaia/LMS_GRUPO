from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'NovoAluno.html')

def recover(request):
    return render(request,'recover.html')

def Professor(request):
    return render(request,'Professor.html')

def Coordenador(request):
	return render(request,'Coordenador.html')
	
