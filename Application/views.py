from django.shortcuts import render
from .models import Sticky
from random import sample


def home(request):
    if request.method == "POST":
        title = request.POST["title"]
        note = request.POST["note"]
        s = Sticky()
        s.title = title
        s.note = note
        slug = unique_slug()
        s.slug = slug
        s.save()
        data = Sticky.objects.all().order_by('-date')[0:5]
        link = "127.0.0.1:8000/app/"+slug
        return render(request, 'application.html', {"Status": "Your Sticky is created!","link": link,"data": data})
    else:
        s = Sticky.objects.all().order_by('-date')[0:5]
        return render(request, 'application.html', {"data": s})


def unique_slug():
    value = "abcdefghijklmnopqrstuvwxyz1234567890"
    sample_slug = sample(value, 6)
    sample_slug = "".join(sample_slug)
    try:
        s = Sticky.objects.get(slug=sample_slug)
        unique_slug()
    except Sticky.DoesNotExist:
        return sample_slug


def display(request, code):
    try:
        s = Sticky.objects.get(slug=code)
        data = Sticky.objects.all().order_by('-date')[0:5]
        return render(request, 'display.html', {"search": s, "data": data})
    except Sticky.DoesNotExist:
        return render(request, 'not_found.html')

