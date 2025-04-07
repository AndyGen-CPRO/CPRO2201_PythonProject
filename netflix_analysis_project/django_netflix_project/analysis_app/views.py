from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from .forms import MediaForm

def media_list(request):
    medias = Media.objects.all()
    return render(request, 'analysis_app/media_list.html', {'medias': medias})

def media_create(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaForm()
    return render(request, 'analysis_app/media_form.html', {'form': form})

def media_update(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == "POST":
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaForm(instance=media)
    return render(request, 'analysis_app/media_form.html', {'form': form})

def media_delete(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == "POST":
        media.delete()
        return redirect('media_list')
    return render(request, 'analysis_app/media_confirm_delete.html', {'media': media})