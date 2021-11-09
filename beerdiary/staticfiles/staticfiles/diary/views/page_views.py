from django.shortcuts import render, redirect
from ..models import Beer
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    beers = Beer.objects.filter(owner=request.user).all()
    my_context = {'my_beers':beers}
    print(beers)
    return render(request, 'diary/index.html', context=my_context)

@login_required
def get_beer(request, beer_id):
    beer = Beer.objects.filter(owner=request.user).get(id=beer_id)
    return render(request,'diary/beer.html', context={'beer':beer})
