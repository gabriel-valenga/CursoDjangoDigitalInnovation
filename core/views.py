from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'Hello {nome} de {idade} anos!')


def soma(request, primnumero, segnumero):
    return HttpResponse(primnumero + segnumero)


def subtracao(request, primnumero, segnumero):
    return HttpResponse(primnumero - segnumero)


def multiplicacao(request, primnumero, segnumero):
    return HttpResponse(primnumero * segnumero)


def divisao(request, primnumero, segnumero):
    return HttpResponse(primnumero / segnumero)


