from django.shortcuts import render
from django.http import HttpResponse
class tarefa(object):
    def __init__(self,titulo,data):
        self.titulo=titulo
        self.data=data
    def __str__(self):
        return self.titulo
def home(request):
    return HttpResponse("Ola")
def sobre(request):
    return HttpResponse("Lucas Scotti")
#def tarefa(request,numero):
    #return HttpResponse("tarefa:"+str(numero))
def tarefa(request,ano,mes,dia):
    return HttpResponse("tarefa:"+str(ano)+"/"+str(mes)+"/"+str(dia))
def contatos(request,contatos):
    return HttpResponse("contato:"+str(contatos))
# Create your views here.
