from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, "app_notas/lista_notas.html", {"notas": notas})

def crear_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_notas")
    else:
        form = NotaForm()
    return render(request, "app_notas/crear_nota.html", {"form": form})

def editar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect("lista_notas")
    else:
        form = NotaForm(instance=nota)
    return render(request, "app_notas/crear_nota.html", {"form": form})

def eliminar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    nota.delete()
    return redirect("lista_notas")
