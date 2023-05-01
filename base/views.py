from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Ingredient
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import CreateUserForm


# Create your views here.


#Aalaap Hegde
#the views for the login page. 
# template_name connects the backend views to the html page
# redirect_authenticated_user ensures the user is signed in 
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ingredients')

#Aalaap Hegde
#the views page to register new users
#template connects to the register html page
# redirect_authenticated_user ensures the user is signed in 
#if registration works, will be redirected to their ingredient list
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('ingredients')

    #checks registration information is valid
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    #redirects to home screen (ingredient list)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('ingredients')
        return super(RegisterPage, self).get(*args, **kwargs)

#Aalaap Hegde
#views for the ingredient list
class IngredientList(LoginRequiredMixin, ListView):
    #model makes each new instance of ingredient a type Ingredient from the Django database
    model = Ingredient
    #renaming the list of ingredients to ingredients
    context_object_name = 'ingredients'


    # Search for user-specific ingredients
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = context['ingredients']
        #search algorithm to find specific ingredients
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['ingredients'] = context['ingredients'].filter(
                ingredientname__icontains=search_input)

        context['search_input'] = search_input
        return context
        
#Aalaap Hegde
#views to show specific details about an ingredient
class IngredientDetail(LoginRequiredMixin, DetailView):
    #model makes each new instance of ingredient a type Ingredient from the Django database
    model = Ingredient
    context_object_name = 'ingredient'
    #template_name = 'xxx.html'

#Aalaap Hegde
#views to create an ingredient
class IngredientCreate(LoginRequiredMixin, CreateView):
    #model makes each new instance of ingredient a type Ingredient from the Django database
    model = Ingredient
    #list of properties of every ingredient object: 
    fields = ['ingredientname','quantity','description']
    success_url = reverse_lazy('ingredients')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IngredientCreate, self).form_valid(form)

#Aalaap Hegde
#helps delete ingredient
class DeleteView(LoginRequiredMixin ,DeleteView):
    #model makes each new instance of ingredient a type Ingredient from the Django database
    model = Ingredient
    context_object_name = 'ingredient'
    success_url = reverse_lazy('ingredients')


def home_page(request):
    context_object_name = 'home'
    template_name = 'base/home.html'

    return render(request, 'base/home.html')
    