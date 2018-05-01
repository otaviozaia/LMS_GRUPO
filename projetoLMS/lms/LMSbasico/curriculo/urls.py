from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from curriculo.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cursos/',cursos, name='cursos'),
    path('detalhecurso/',detalhecurso, name='detalhecurso'),
    path('detalhedisciplina/',detalhedisciplina, name='detalhedisciplina'),
    path('disciplinascurso/',disciplinascurso, name='disciplinascurso'),
    path('login/', auth_views.login,{'template_name': 'login.html'}, name='login'),
    path('matricula/',matricula, name='matricula'),
    path('novadisciplina/',novaDisciplina, name='novaDisciplina'),
    path('novocurso/',novo_curso, name='novo_curso'),
    path('novoaluno/',NovoAluno, name='NovoAluno'),
    path('recover/',recover, name='recover'),
	path('Professor/',Professor, name='Professor'),
	path('Coordenador/',Coordenador, name='Coordenador')

]
