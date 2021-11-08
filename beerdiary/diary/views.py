from django.shortcuts import render
from .models import Beer


# Create your views here.
def index(request):
    beers = Beer.objects.all()
    my_context = {'my_beers':beers}
    return render(request, 'diary/index.html', context=my_context)