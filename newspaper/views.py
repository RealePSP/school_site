from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from klasses.models import Klass
from .models import ClassNewspaper
from .forms import ClassNewspaperForm

@login_required
def newspaper_create(request, klass_id):
    klass = get_object_or_404(Klass, id=klass_id)
    if request.user.klass != klass:
        return HttpResponseForbidden("Доступ запрещён")
    if request.method == 'POST':
        form = ClassNewspaperForm(request.POST, request.FILES)
        if form.is_valid():
            newspaper = form.save(commit=False)
            newspaper.klass = klass
            newspaper.save()
            return redirect('class_detail', pk=klass.id)
    else:
        form = ClassNewspaperForm()
    return render(request, 'newspaper_form.html', {'form': form, 'klass': klass})

@login_required
def newspaper_edit(request, pk):
    newspaper = get_object_or_404(ClassNewspaper, pk=pk)
    if request.user.klass != newspaper.klass:
        return HttpResponseForbidden("Доступ запрещён")

    if request.method == 'POST':
        form = ClassNewspaperForm(request.POST, request.FILES, instance=newspaper)
        if form.is_valid():
            form.save()
            return redirect('class_detail', pk=newspaper.klass.id)
    else:
        form = ClassNewspaperForm(instance=newspaper)
    return render(request, 'newspaper_form.html', {'form': form, 'klass': newspaper.klass})

@login_required
def newspaper_delete(request, pk):
    newspaper = get_object_or_404(ClassNewspaper, pk=pk)
    if request.user.klass != newspaper.klass:
        return HttpResponseForbidden("Доступ запрещён")
    
    if request.method == 'POST':
        newspaper.delete()
        return redirect('class_detail', pk=newspaper.klass.id)
    
    return render(request, 'newspaper_confirm_delete.html', {'newspaper': newspaper})
