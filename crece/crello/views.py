from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from crello.models import *

def index(request):
    return render(request,'crello/index.html',{})

class TableroForm(ModelForm):
    class Meta:
        model = Tablero
        fields =['nombre']

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields =['nombre','fk_Tablero']

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields =['nombre','descripcion','fk_Lista']

def crear_tab(request):
    templ = 'crello/crear_tablero.html'
    form =  TableroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultar_tab')
    return render(request,templ,{'form':form})

def crear_lista(request):
    templ = 'crello/crear_Lista.html'
    form =  ListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        #return redirect('consultar_')# tiene que dirigir a otro
    return render(request,templ,{'form':form})

def consultar_tab(request):
    templ = 'crello/contenedorTablero.html'
    listado_tablero=Tablero.objects.all()
    contexto={}
    contexto['objectlist']=listado_tablero
    return render(request,templ,contexto)

def consultar_lista(request):
    templ = 'crello/tablero.html'
    listado_lista=Lista.objects.all()
    contexto={}
    contexto['objectlist']=listado_lista
    return render(request,templ,contexto)

def editar_tab(request,id):
    template = 'crello/editar_tablero.html'
    info_Tablero = get_object_or_404(Tablero, pk=id)
    form = TableroForm(request.POST or None, instance=info_Tablero)
    if form.is_valid():
        form.save()
        return redirect('consultar_tab')
    return render(request,template,{'form':form})

def eliminar_tab(request,id):
    template = 'crello/eliminar_tablero.html'
    info_Tablero = get_object_or_404(Tablero, pk=id)
    if request.method == 'POST':
        info_Tablero.delete()
        return redirect('consultar_tab')
    return render(request,template,{'info_Tablero':info_Tablero})

