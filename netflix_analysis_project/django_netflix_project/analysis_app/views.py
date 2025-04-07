from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from .forms import MediaForm
from django.db.models import Q, Min, Max

def media_list(request):
    query = request.GET.get('q', '')
    type = request.GET.get('type', '')
    year = request.GET.get('year', '')
    country = request.GET.get('country', '')
    genre = request.GET.get('genre', '')

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
        medias = medias.filter(country__icontains=country)
    
    if genre:
        medias = medias.filter(listed_in__icontains=genre)

    #To get the range of all the years present in the dataset
    min_year = Media.objects.aggregate(Min('release_year'))['release_year__min'] or 1900
    max_year = Media.objects.aggregate(Max('release_year'))['release_year__max'] or 2025
    all_years = list(range(min_year, max_year + 1))

    #Filtering the countries present in the dataset that was separated by commas
    raw_countries = Media.objects.values_list('country', flat=True)

    country_set = set()
    for entry in raw_countries:
        if entry:
            country_list = [c.strip() for c in entry.split(',') if c.strip()]
            country_set.update(country_list)

    all_countries = sorted(country_set)
    all_countries.insert(0, 'Empty')

    #Filtering the genre/catagories present in the dataset
    raw_genres = Media.objects.values_list('listed_in', flat=True)

    genre_set = set()
    for entry in raw_genres:
        if entry:
            genre_list = [g.strip() for g in entry.split(',') if g.strip()]
            genre_set.update(genre_list)
    
    all_genres = sorted(genre_set)

    context = {
        'medias': medias,
        'types': Media.objects.values_list('type', flat=True).distinct(),
        'years': all_years,
        'countries': all_countries,
        'genres': all_genres
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