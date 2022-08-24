from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *



@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "orcamento.html", contexto)