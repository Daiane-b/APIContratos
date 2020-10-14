from django.db import models
from datetime import date

STATUS = (
    (1, 'criado'),
    (2,'aguardando_docs'),
    (3,'aprovado'),
    (4,'analisado')
)
STATUS_APROVACAO = (
    (1,'analisando'),
    (2,'aprovado'),
    (3,'rejeitado')
)
TIPO_DOC = (
    (1,'CPF'),
    (2,'CNH')
)
class User(models.Model):
   nome = models.CharField(max_length=30, null=False)
   email = models.EmailField(null=False)
   cpf = models.CharField(null=False, max_length=30)
   renda = models.FloatField(null=False)
   rua = models.CharField(max_length=60, blank=True)
   numero = models.IntegerField(default=0)
   bairro = models.CharField(max_length=30,  blank=True)
   cidade = models.CharField(max_length=30,  blank=True)
   estado = models.CharField(max_length=2,  blank=True)
   estadoCivil = models.CharField(max_length=30,  blank=True)
   dataNascimento = models.DateField(max_length=30,  default=date.today())

class Contrato(models.Model):
   valor = models.FloatField(null=False, default=0)
   status = models.CharField(choices=STATUS,
    null=False, max_length=50, default=STATUS[0])
   usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
   statusAprovacao = models.CharField(choices=STATUS_APROVACAO,
                             null=False, max_length=50, blank=True)
class Documento(models.Model):
    tipo = models.CharField(choices=TIPO_DOC,
                                       null=False, max_length=50, default=TIPO_DOC[0])
    urlimagens = models.CharField(max_length=1000, blank=True)
    urlcomprovanteRenda = models.CharField(max_length=1000, blank=True)
    contratoId = models.ForeignKey(Contrato, on_delete=models.CASCADE)
# Create your models here.
