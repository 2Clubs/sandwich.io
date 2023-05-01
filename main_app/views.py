from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sandwich, Ingredient


# Create your views here.
def home(request):
    return render(request,'home.html')

 
@login_required
def sandwich_index(request):
  sandwiches = Sandwich.objects.filter(user=request.user)
  return render(request, 'sandwiches/index.html', {'sandwiches': sandwiches})


@login_required
def sandwich_detail(request, sandwich_id):
    sandwich = Sandwich.objects.get(id=sandwich_id)
    ingredients_sandwich_doesnt_have = Ingredient.objects.exclude(id__in = sandwich.ingredients.all().values_list('id'))
    return render(request, 'sandwiches/detail.html', {
    'sandwich': sandwich, 'ingredients': ingredients_sandwich_doesnt_have,
  })


@login_required
def assoc_ingredient(request, sandwich_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Sandwich.objects.get(id=sandwich_id).ingredients.add(ingredient_id)
  return redirect('detail', sandwich_id=sandwich_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class SandwichUpdate(LoginRequiredMixin, UpdateView):
  model = Sandwich
  fields = ['temp', 'description']

class SandwichDelete(LoginRequiredMixin, DeleteView):
  model = Sandwich
  success_url = '/'
