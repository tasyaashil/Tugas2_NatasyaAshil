from django.shortcuts import render
from katalog.models import CatalogItem

nama_mhs = 'Natasya Ashil Zhafirah'
studentid = '2106650090'

# TODO: Create your views here.
def index(request):
    response = {'nama_mhs' : nama_mhs, 'studentid' : studentid, 'item_data' : CatalogItem.objects.all() }
    return render(request, 'katalog.html', response)
