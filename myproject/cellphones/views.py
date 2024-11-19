from django.shortcuts import render, redirect, get_object_or_404
from .models import Cellphone
from .forms import CellphoneForm

def cellphone_list(request):
    cellphones = Cellphone.objects.all()
    return render(request, 'cellphones/cellphone_list.html', {'cellphones': cellphones})

def cellphone_create(request):
    if request.method == "POST":
        form = CellphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cellphone_list')
    else:
        form = CellphoneForm()
    return render(request, 'cellphones/cellphone_form.html', {'form': form})

def cellphone_update(request, pk):
    cellphone = get_object_or_404(Cellphone, pk=pk)
    if request.method == "POST":
        form = CellphoneForm(request.POST, instance=cellphone)
        if form.is_valid():
            form.save()
            return redirect('cellphone_list')
    else:
        form = CellphoneForm(instance=cellphone)
    return render(request, 'cellphones/cellphone_form.html', {'form': form})

def cellphone_delete(request, pk):
    cellphone = get_object_or_404(Cellphone, pk=pk)
    if request.method == "POST":
        cellphone.delete()
        return redirect('cellphone_list')
    return render(request, 'cellphones/cellphone_confirm_delete.html', {'cellphone': cellphone})