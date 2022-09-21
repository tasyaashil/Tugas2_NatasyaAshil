from mywatchlist.views import show_mywatchlist, show_mywatchlistxml, show_mywatchlistjson
from django.urls import path

app_name = 'wishlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlistxml, name='show_mywatchlistxml'), 
    path('json/', show_mywatchlistjson, name='show_wishlistjson'), 

]