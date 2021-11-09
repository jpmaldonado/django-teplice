from django.views import View
from django.shortcuts import redirect, render
from ..forms import EntryForm, BeerForm
from django.contrib.auth.decorators import login_required

@login_required
def add_beer(request):
    if request.method != 'POST':
        form = BeerForm()
    else:
        # User clicked submit, POST request to process data
        form = BeerForm(data=request.POST)

        # Add form validation
        if form.is_valid():
            new_beer = form.save(commit=False)
            new_beer.owner = request.user
            new_beer.save()
            return redirect('diary:index')

    context = {'form':form}
    return render(request,'diary/add_beer.html', context=context)

class AddEntry(View):
    def get(self, request):
        form = EntryForm()
        context = {'form':form}
        return render(request,'diary/add_entry.html', context=context)

    def post(self, request):
        form = EntryForm(data=request.POST)
        # Add form validation
        if form.is_valid():
            form.save()
            return redirect('diary:index')
