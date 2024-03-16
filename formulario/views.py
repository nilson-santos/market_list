from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from .models import Item
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            all = Item.objects.filter(Q(item__icontains=search)).order_by('-created_at')
        else:
            all = Item.objects.all().order_by('-created_at')
        
        paginator = Paginator(all, 4)
        pages = request.GET.get('page')
        items = paginator.get_page(pages)
        context = {'items': items}
        return render(request, 'partials/lista.html', context)


def lista(request):
    search = request.GET.get('search')
    if search:
        all = Item.objects.filter(Q(item__icontains=search)).order_by('-created_at')
    else:
        all = Item.objects.all().order_by('-created_at')

    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    items = paginator.get_page(pages)
    context = {'items': items}
    return render(request, 'lista.html', context)


def item_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Criado')
        return redirect('item_lista')

    context = {'form': form}
    items = Item.objects.all()
    return render(request, 'create_item.html', context)


def item_update(request, id):
    item = get_object_or_404(Item, pk=id)
    form = PostForm(request.POST or None, instance=Item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Atualizado')
        return redirect('item_lista')

    context = {'form': form, 'item': item}
    return render(request, 'update_item.html', context)


def item_delete(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Excluído')
        return redirect('item_lista')

    context = {'item': item}
    return render(request, 'delete_confirm.html', context)
