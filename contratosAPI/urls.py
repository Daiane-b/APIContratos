from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^addContrato', ContratoInsert.as_view()),
    url(r'^contrato/(?P<pk>[0-9]+)$', ContratoView.as_view()),
    url(r'^addDoc', AddDoc.as_view()),
]