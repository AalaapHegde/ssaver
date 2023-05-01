from django.urls import path
from .views import IngredientList, IngredientDetail, IngredientCreate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views

#connects all the urls to their corresponding 'buttons'
#list of URLS
urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', views.home_page, name='home'),

    path('ingredients/', IngredientList.as_view(), name = 'ingredients'),
    path('ingredient/<int:pk>', IngredientDetail.as_view(), name = 'ingredient'), 
    path('ingredient-create/', IngredientCreate.as_view(), name = 'ingredient-create'),
    path('ingredient-delete/<int:pk>/', DeleteView.as_view(), name = 'ingredient-delete'),

]