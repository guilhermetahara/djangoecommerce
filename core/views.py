from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	texto = ['Este é um e-commerce programado em python 3 com framework Django!']
	context = {
		'title' : 'Django e-commerce',
		'text' : texto
	}
	return render(request, 'index.html', context)

def contato(request):
	
	return render(request, 'contact.html')


def produto(request):

	
	return render(request, 'product.html')


def lista_produto(request):

	
	return render(request, 'product_list.html')
