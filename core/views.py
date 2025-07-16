from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:registro')
    else:
        form = RegistroForm()
    registros = Registro.objects.all().order_by('fecha_registro')
    return render(request, 'core/registro.html', {'form': form, 'registros': registros})

def mostrarHTML(request):
    return render(request, 'muestra.html')
