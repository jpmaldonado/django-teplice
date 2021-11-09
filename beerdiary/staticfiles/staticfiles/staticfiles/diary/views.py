from django.shortcuts import render
from .models import Beer


# Create your views here.
def index(request):
    beers = Beer.objects.all()
    my_context = {'my_beers':beers}
    print(beers)
    return render(request, 'diary/index.html', context=my_context)

def get_beer(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    return render(request,'diary/beer.html', context={'beer':beer})