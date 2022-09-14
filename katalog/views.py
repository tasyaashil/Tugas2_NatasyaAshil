from django.shortcuts import render
from katalog.models import CatalogItem
import json

nama_mhs = 'Natasya Ashil Zhafirah'
studentid = '2106650090'

f = open('C:\\PBP\\Tugas2\\Tugas2_NatasyaAshil\\katalog\\fixtures\\initial_catalog_data.json', 'r')
item_data = json.loads(f.read())

item = []
for barang in item_data:
    item.append(CatalogItem(item_name = barang ['fields']['item_name'],
    item_price = barang ['fields']['item_price'],
    item_stock = barang ['fields']['item_stock'],
    rating = barang ['fields']['rating'],
    description = barang ['fields']['description'],
    item_url = barang ['fields']['item_url']))

# TODO: Create your views here.
def index(request):
    response = {'name' : nama_mhs, 'studentid' : studentid, 'item_data' : item }
    return render(request, 'katalog.html', response)
