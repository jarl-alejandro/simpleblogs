from django.shortcuts import render
from principal.models import Entrada

def inicio(request):
	entradas = Entrada.objects.all()
	return render(request, "inicio.html", { 'entradas':entradas })