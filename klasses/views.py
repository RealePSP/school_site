from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Klass
from .forms import KlassForm

@login_required
def klass_edit(request, pk):
    klass = get_object_or_404(Klass, pk=pk)
    if request.method == 'POST':
        form = KlassForm(request.POST, instance=klass)
        if form.is_valid():
            form.save()
            return redirect('class_detail', pk=klass.pk)
    else:
        form = KlassForm(instance=klass)
    return render(request, 'klasses/class_edit.html', {'form': form})

def class_list(request):
    klasses = Klass.objects.all()
    return render(request, 'klasses/class_list.html', {'klasses': klasses})

def class_detail(request, pk):
    klass = get_object_or_404(Klass, pk=pk)
    return render(request, 'klasses/class_detail.html', {'klass': klass})

def class_students(request, pk):
    klass = get_object_or_404(Klass, pk=pk)
    profiles = klass.profiles.all()
    return render(request, 'klasses/class_students.html', {'klass': klass, 'profiles': profiles})
