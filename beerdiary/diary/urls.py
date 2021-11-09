from .views.form_views import add_beer, AddEntry
from .views.page_views import index, get_beer
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'diary'
urlpatterns = [
    path('', view=index, name='index'),
    path('beer/<int:beer_id>', view=get_beer, name='beer'),
    path('beer/add/', view=add_beer, name='add_beer'),
    path('beer/add/entry/', view=login_required(AddEntry.as_view()), name='add_entry'),
]