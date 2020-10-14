from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nome", "email", "cpf",
                  "renda", "rua", "numero", "bairro", "cidade", "estado", "estadoCivil", "dataNascimento"]

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ["id", "valor", "status", "usuarioId", "statusAprovacao"]

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ["id", "tipo", "urlimagens", "urlcomprovanteRenda", "contratoId"]