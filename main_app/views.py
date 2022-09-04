from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Nft, Chain

from .forms import RatingForm



def home(request):
    return render(request, 'nft/home.html')

def about(request):
    return render(request, 'about.html')

def allCollection(request):
    nfts = Nft.objects.all()
    return render(request, 'allCollection.html', {'nfts': nfts})

def nftDetails(request, nft_id):
    nfts = Nft.objects.get(id=nft_id)
    rating_form = RatingForm()

    return render(request, 'nft/detail.html', {'nfts': nfts, 'rating_form': rating_form})

class NftCreate(CreateView):
    model = Nft
    fields = '__all__' #['name', 'description', 'type', 'price'] <- telling django what keys on the model we want to genrate the form with.
    

class nftUpdate(UpdateView):
    model = Nft
    fields = '__all__'
        

class nftDelete(DeleteView):
    model = Nft
    success_url = '/allCollection/'


def add_rating(request, nft_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.nft_id = nft_id
        new_rating.save()
    return redirect('detail', nft_id = nft_id)    




class ChainList(ListView):
  model = Chain

class ChainDetail(DetailView):
  model = Chain

class ChainCreate(CreateView):
  model = Chain
  fields = '__all__'
  success_url = '/chain/'

class ChainUpdate(UpdateView):
  model = Chain
  fields = ['name', 'color']

class ChainDelete(DeleteView):
  model = Chain
  success_url = '/chain/'