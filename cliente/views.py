from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cliente

def index(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        cpf_cnpj = request.POST["cpf"]
        tipo = request.POST["tipo"]

        cliente = {
            "nome":nome,
            "cpf" :cpf_cnpj,
            "tipo": tipo
        }
        return redirect(to="cliente:list", context={"cliente" : cliente})
    else:
        return render(request,"index.html")
def lista(request):
    clientes = Cliente.objects.all()
    return render(request, "lista.html",
    context={"clientes":clientes, 
    "titulo":"Lista de clientes"})
def detalhe(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, "detalhe.html" , context={"cliente":cliente})
def contato(request):
    return render(request,"contatos.html")

