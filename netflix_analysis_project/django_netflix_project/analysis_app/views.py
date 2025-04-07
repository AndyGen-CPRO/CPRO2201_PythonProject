from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from .forms import MediaForm
from django.db.models import Q

def media_list(request):
    query = request.GET.get('q', '')
    type = request.GET.get('type', '')
    year = request.GET.get('year', '')
    country = request.GET.get('country', '')

    medias = Media.objects.all()

    if query:
        medias = medias.filter(
            Q(title__icontains=query) |
            Q(director__icontains=query) |
            Q(cast__icontains=query)
        )
    
    if type:
        medias = medias.filter(type=type)

    if year:
        medias = medias.filter(release_year=year)

    if country:
        medias = medias.filter(country=country)

    context = {
        'medias': medias,
        'types': Media.objects.values_list('type', flat=True).distinct(),
        'years': Media.objects.values_list('release_year', flat=True).distinct(),
        'countries': Media.objects.values_list('country', flat=True).distinct()
    }
    return render(request, 'analysis_app/media_list.html', context)

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