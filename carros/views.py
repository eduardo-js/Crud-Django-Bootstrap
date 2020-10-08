from django.shortcuts import render

# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from carros.forms import CarroForm
from carros.models import Carro


def welcome(request):
    return render(request, "welcome.html");


def lista(request):
    lista_itens = Carro.objects.all()
    return render(request, "lista.html", {'lista_itens': lista_itens})


def adiciona(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "salvo.html", {})
    else:
        form = CarroForm()
        return render(request, "adiciona.html", {'form': form})


def editar(request, nr_item):
    if request.method == 'GET':
        carro = get_object_or_404(Carro, pk=nr_item)
        form = CarroForm(instance=carro)
        return render(request, 'editar.html', {'form': form, 'carro': carro})
    if request.method == 'POST':
        carro = get_object_or_404(Carro, pk=nr_item)
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return render(request, "salvo.html", {})
    return adiciona(request)


def excluir(request, nr_item):
    get_object_or_404(Carro, pk=nr_item).delete()
    return lista(request)
