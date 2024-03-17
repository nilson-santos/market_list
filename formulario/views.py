from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from .models import Item
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def hide_items(request):
    cookie = request.COOKIES.get('hide_items')
    response = redirect('item_lista')
    if cookie == 'show' or cookie is None:
        response.set_cookie('hide_items', 'hide')
    else:
        response.set_cookie('hide_items', 'show')
    return response


def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        cookie = request.COOKIES.get('hide_items')
        if cookie != 'hide':
            all = Item.objects.filter(Q(item__icontains=search)).order_by('category', 'item')
        else:
            all = Item.objects.filter(Q(item__icontains=search) & (~Q(amount__isnull=True) & ~Q(amount=''))).order_by('category', 'item')
        paginator = Paginator(all, 10)
        pages = request.GET.get('page')
        items = paginator.get_page(pages)
        context = {'items': items, 'cookie': cookie}
        return render(request, 'partials/lista.html', context)


def lista(request):
    search = request.GET.get('search')
    cookie = request.COOKIES.get('hide_items')
    if cookie != 'hide':
        all = Item.objects.all().order_by('category', 'item')
    else:
        all = Item.objects.exclude(amount__isnull=True).exclude(amount='').order_by('category', 'item')
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    items = paginator.get_page(pages)
    context = {'items': items, 'cookie': cookie}
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
    form = PostForm(request.POST or None, instance=item)
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


@csrf_exempt
def on_cart(request, id):
    item = get_object_or_404(Item, pk=id)
    on_cart = item.on_cart
    Item.objects.filter(id=id).update(on_cart=not on_cart)

    return redirect('item_lista')
