from datetime import datetime  
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class ContasManager(BaseUserManager):
        use_in_migrations = True
        def _create_user(self,username,password,**extra_fields):
                if not username:
                        raise ValueError('Coloque o username')
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        def create_user(self, username, password=None, **extra_fields):
                return self._create_user(username, password, **extra_fields)

        def create_superuser(self, username, password, **extra_fields):
                extra_fields.setdefault('is_staff', True)
                extra_fields.setdefault('is_superuser', True)


                if extra_fields.get('is_staff') is not True:
                    raise ValueError('Superuser must have is_staff=True.')
                if extra_fields.get('is_superuser') is not True:
                    raise ValueError('Superuser must have is_superuser=True.')

                return self._create_user(username, password, **extra_fields)

class User(PermissionsMixin,AbstractBaseUser):
    username = models.CharField('Login',max_length=50,unique=True)
    password = models.CharField('Senha',max_length=20)
    name = models.CharField('Nome',max_length=100)
    email = models.EmailField('Email',unique=True)
    celular = models.CharField('Celular',max_length=11)
    dtExpiracao = models.DateField('Data de Expiração',default='1900-01-01')
    tipo = models.CharField(max_length=1,default='C')
    is_active = models.BooleanField(blank=True,default=True)
    is_staff = models.BooleanField(blank=True,default=False)
    date_joined = models.DateTimeField('Data de Cadastro',auto_now_add=True)

    objects = ContasManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    class meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Professor(User):
        apelido = models.CharField(max_length=30)


class Aluno(User):
        ra = models.CharField(max_length=7)
        foto = models.ImageField()

class Disciplina(models.Model):
        nome = models.CharField(max_length=60, unique=True)
        data = models.DateTimeField(default=datetime.now())
        status = models.CharField(max_length=7, default='Aberta')
        planoDeEnsino = models.TextField()
        cargaHoraria = models.SmallIntegerField()
        competencias = models.TextField()
        habilidades = models.TextField()
        ementa = models.TextField()
        conteudoProgramatico = models.TextField()
        bibliografiaBasica = models.TextField()
        bibliografiaComplementas = models.TextField()
        percentualPratico = models.SmallIntegerField()
        percentualTeorico = models.SmallIntegerField()
        Coordenador = models.OneToOneField('curriculo.User',null=True,on_delete = models.DO_NOTHING)


class Curso(models.Model):
        nome = models.CharField(max_length=60,unique=True)


        
class DisciplinaOfertada(models.Model):
        idCoordenador = models.ForeignKey(User,null=True,on_delete = models.DO_NOTHING)
        DTInicioMatricula = models.DateField(null=True,blank = True)
        DTFimMatricula = models.DateField(null=True,blank = True)
        idDisciplina = models.ForeignKey(Disciplina,null=True,on_delete = models.DO_NOTHING)
        idCurso = models.ForeignKey(Curso,null=True,on_delete = models.DO_NOTHING)
        ano = models.SmallIntegerField()
        semestre = models.CharField(max_length=1,null=False)
        turma = models.CharField(max_length=1,null=False)
        idProfessor = models.ForeignKey(Professor,related_name='idprofessor',null=True,on_delete = models.DO_NOTHING)
        metodologia = models.TextField(null=True)
        recursos = models.TextField(null=True)
        criterioAvaliacao = models.TextField(null=True)
        planoDeAulas = models.TextField(null=True)

class SolicitacaoMatricula(models.Model):
        idAluno = models.ForeignKey(Aluno,null=True,on_delete = models.DO_NOTHING)
        idDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada,null=True,on_delete = models.DO_NOTHING)
        DTSolicitacao = models.DateTimeField(default = datetime.now())
        idCoordenador = models.ForeignKey(User,null=True,related_name='idCoordenador',on_delete = models.DO_NOTHING)
        status = models.CharField(max_length=10,default='Solicitada')

class Atividade(models.Model):
        titulo = models.CharField(max_length=60)
        descricao = models.TextField(null=True,blank=True)
        conteudo = models.TextField(null=True,blank=True)
        tipo = models.CharField(max_length=15,default='Resposta Aberta')
        extras = models.TextField(null=True,blank=True)
        idProfessor = models.ForeignKey(Professor,null=True,on_delete = models.DO_NOTHING)

class AtividadeVinculada(models.Model):
        idAtividade = models.ForeignKey(Atividade,null=True,on_delete = models.DO_NOTHING)
        idProfessor = models.ForeignKey(Professor,null=True,on_delete = models.DO_NOTHING)
        idDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada,null=True,on_delete = models.DO_NOTHING)
        rotulo = models.SlugField(max_length=6)
        status = models.CharField(max_length=15)
        DtInicioRespostas = models.DateField()
        DtFimRespostas = models.DateField()

class Entrega(models.Model):
       idAluno = models.ForeignKey(Aluno,null=True,on_delete = models.DO_NOTHING)
       idAtividadeVinculada=models.ForeignKey(AtividadeVinculada,null=True,on_delete=models.DO_NOTHING)
       Titulo=models.CharField(max_length=60)
       Reposta=models.TextField()
       DtEntrega=models.DateTimeField(default=datetime.now())
       StatusEntrega=models.CharField(max_length=9,default='Entregue') 
       idProfessor=models.ForeignKey(Professor,null=True,on_delete = models.DO_NOTHING)
       Nota=models.DecimalField(max_digits=3,decimal_places=0)
       DtAvaliacao=models.DateField()
       Obs=models.TextField(null=True,blank=True)

class Mensagem(models.Model):
        idAluno = models.ForeignKey(Aluno,null=True,on_delete = models.DO_NOTHING)
        idProfessor = models.ForeignKey(Professor,null=True,on_delete = models.DO_NOTHING)
        Assunto = models.CharField(max_length=60)
        Referencia = models.CharField(max_length=200)
        Conteudo = models.TextField()
        StatusMensagem = models.CharField(max_length=10,default='Entregue')
        DTEnvio = models.DateTimeField(default = datetime.now())
        DTResposta = models.DateTimeField(null=True,blank=True)
        resposta = models.TextField()
        
        
        
        

        
        
        
        

        
