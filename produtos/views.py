from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all()  # <- Isso é essencial
    return render(request, 'produtos/lista.html', {'produtos': produtos})

# def adicionar_produto(request):
#     if request.method == 'POST':
#         nome = request.POST['nome']
#         preco = request.POST['preco']
#         Produto.objects.create(nome=nome, preco=preco)
#         return redirect('lista_produtos')
#     return render(request, 'produtos/formulario.html')

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/formulario.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/formulario.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})