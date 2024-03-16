from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from .models import Person
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            all = Person.objects.filter(Q(nome__icontains=search) | Q(sobrenome__icontains=search)).order_by('-created_at')
        else:
            all = Person.objects.all().order_by('-created_at')
        
        paginator = Paginator(all, 4)
        pages = request.GET.get('page')
        persons = paginator.get_page(pages)
        context = {'persons': persons}
        return render(request, 'partials/lista.html', context)


def lista(request):
    # persons = Person.objects.all()
    search = request.GET.get('search')
    if search:
        all = Person.objects.filter(Q(nome__icontains=search) | Q(sobrenome__icontains=search)).order_by('-created_at')
    else:
        all = Person.objects.all().order_by('-created_at')

    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    persons = paginator.get_page(pages)
    context = {'persons': persons}
    return render(request, 'lista.html', context)


def nome_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Criado')
        return redirect('nome_lista')

    context = {'form': form}
    persons = Person.objects.all()
    return render(request, 'create_nome.html', context)


def nome_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PostForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        messages.success(request, 'Atualizado')
        return redirect('nome_lista')

    context = {'form': form, 'person': person}
    return render(request, 'update_nome.html', context)


def nome_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        messages.success(request, 'Excluído')
        return redirect('nome_lista')

    context = {'person': person}
    return render(request, 'delete_confirm.html', context)