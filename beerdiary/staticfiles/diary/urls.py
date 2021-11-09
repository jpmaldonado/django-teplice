from .views import index, get_beer
from django.urls import path

app_name = 'diary'
urlpatterns = [
    path('', view=index, name='index'),
    path('beer/<int:beer_id>', view=get_beer, name='beer'),
]