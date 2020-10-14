from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Create your views here.
class ContratoInsert(APIView):
    def post(self, request):
        try:
            userSerializer = UserSerializer(data=request.data)
            if userSerializer.is_valid():
                user = userSerializer.save()
                if (user.id):
                    contratoAdd = request.data
                    contratoAdd['usuarioId'] = user.id
                    contratoSerializer = ContratoSerializer(data=contratoAdd)
                    if contratoSerializer.is_valid():
                        contratoSerializer.save()
                    else:
                        return Response("Contrado não inserido, erro: "+contratoSerializer.errors, status=status.HTTP_400_BAD_RESQUEST)
            else:
                return Response(userSerializer.errors, status=status.HTTP_400_BAD_RESQUEST)
            return JsonResponse({"Contrato": contratoSerializer.data, "User": userSerializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'mensagem': "Ocorreu um erro: "+e},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ContratoView(APIView):
    def get(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            contrato = Contrato.objects.get(pk=pk)
            contratoSerializer = ContratoSerializer(contrato)
            user = User.objects.get(pk=contratoSerializer.data['usuarioId'])
            userSerializer = UserSerializer(user)
            return JsonResponse({'contrato':contratoSerializer.data, 'usuario': userSerializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'mensagem': "Ocorreu um erro:"},
                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O id deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            contrato = Contrato.objects.get(pk=pk)
            serializer = ContratoSerializer(contrato, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Contrato.DoesNotExist:
            return JsonResponse({'mensagem': "O contrato não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            print(ex)
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O id deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            contrato = Contrato.objects.get(pk=pk)
            contrato.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contrato.DoesNotExist:
            return JsonResponse({'mensagem': "O contrato não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddDoc(APIView):
    def post(self, request):
        try:
            documentoSerializer = DocumentoSerializer(data=request.data)
            if documentoSerializer.is_valid():
                doc = documentoSerializer.save()
                if (doc.id):
                    Contrato.objects.filter(pk=doc.contratoId).update(statusAprovacao=2)
            else:
                return Response(documentoSerializer.errors, status=status.HTTP_400_BAD_RESQUEST)
            return JsonResponse(documentoSerializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"+ex},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
