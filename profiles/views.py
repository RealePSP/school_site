from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Profile, Klass
from .forms import ProfileForm

@login_required
def profile_create(request, klass_id):
    klass = get_object_or_404(Klass, id=klass_id)
    if request.user.klass != klass:
        return HttpResponseForbidden("Доступ запрещён")
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)  # Добавляем request.FILES
        if form.is_valid():
            profile = form.save(commit=False)
            profile.klass = klass
            profile.save()
            return redirect('class_detail', pk=klass.id)
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    klass = get_object_or_404(Klass, id=profile.klass.id)
    if request.user.klass != klass:
        return HttpResponseForbidden("Доступ запрещён")
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('class_students', pk=profile.klass.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    klass = get_object_or_404(Klass, id=profile.klass.id)
    if request.user.klass != klass:
        return HttpResponseForbidden("Доступ запрещён")
    if request.method == 'POST':
        profile.delete()
        return redirect('class_students', pk=profile.klass.id)
    return render(request, 'profile_confirm_delete.html', {'profile': profile})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})
