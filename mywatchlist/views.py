from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import watchlistmovie

# Create your views here.
def show_mywatchlist(request):
    data = watchlistmovie.objects.all()
    context = {
    'list_movie': data,
    'nama': 'Natasya Ashil Zhafirah',
    'npm' : '2106650090'
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlistxml(request):
    data = watchlistmovie.objects.all()
    context = {
    'list_movie': data,
    'nama': 'Natasya Ashil Zhafirah',
    'npm' : '2106650090'
    }
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlistjson(request):
    data = watchlistmovie.objects.all()
    context = {
    'list_movie': data,
    'nama': 'Natasya Ashil Zhafirah',
    'npm' : '2106650090'
    }
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")