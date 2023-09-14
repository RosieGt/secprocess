from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import PedidoForm
from django.contrib import messages


from .models import Pedido

@login_required
def base(request):
    
    return render(request,'base.html')
@login_required
def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.done = 'doing'
            form.save()
            return redirect('/listar/')
        else:
            form = PedidoForm()
            return render(request, 'pedidos/cadastrar_pedido.html', {'form': form}) 
    else:
        form = PedidoForm()
        return render(request, 'pedidos/cadastrar_pedido.html', {'form': form})
@login_required
def listar_pedido(request):
    
    search = request.GET.get('search')
    
    filter = request.GET.get('filter')
    pedidosDone = Pedido.objects.filter(done='done').count()
    pedidosDoing = Pedido.objects.filter(done='doing').count()
   
   
    if search:
        
        pedidos = Pedido.objects.filter(nome__icontains=search)
    
    elif filter:
        pedidoss = Pedido.objects.filter(done=filter)
        
    else:
        pedido_list = Pedido.objects.all().order_by('-created_at')
    
        paginator = Paginator(pedido_list, 5)
    
        page = request.GET.get('page')
    
        pedidos = paginator.get_page(page)
      
    return render(request, 'pedidos/listar_pedido.html', 
                  {'pedidos' : pedidos, 'pedidosdone': pedidosDone, 'pedidosdoing': pedidosDoing })
@login_required
def pedidoView(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    return render(request, 'pedidos/detalhar_pedido.html', 
                  {'pedido': pedido })
@login_required
def editPedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    form = PedidoForm(instance=pedido)

    if(request.method == 'POST'):
        form = PedidoForm(request.POST, instance=pedido)

        if(form.is_valid()):
            pedido.save()
            return redirect('/listar/')
        else:
            return render(reuquest, 'pedidos/atualizar_pedido.html', {'form': form, 'pedido': pedido})
    else:
        return render(request, 'pedidos/atualizar_pedido.html', {'form': form, 'pedido': pedido})
@login_required
def deletePedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.delete()

    messages.info(request, 'Pedido deletado com sucesso.')

    return redirect('/listar/') 
@login_required
def changeStatus(request, id):
    pedido = get_object_or_404(Pedido, pk=id)

    if(pedido.done == 'doing'):
        pedido.done = 'done'
    else:
        pedido.done = 'doing'

    pedido.save()

    return redirect('/listar/')

def pedido_finalizado(request):
    search = request.GET.get('search')
    
    # filter = request.GET.get('filter')
    #pedidosDone = Pedido.objects.filter(done='done')
   
   
    if search:
        
        pedidos = Pedido.objects.filter(nome__icontains=search)
    
    #elif filter:
       # pedidos = Pedido.objects.filter(done=filter)
        
    else:
        pedido_list = Pedido.objects.filter(done='doing').order_by('-created_at')
    
        paginator = Paginator(pedido_list, 10)
    
        page = request.GET.get('page')
    
        pedidos = paginator.get_page(page)
      
    return render(request, 'pedidos/pedido_finalizado.html', 
                  {'pedidos' : pedidos})
   