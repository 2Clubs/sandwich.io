from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('ingredients/', views.IngredientsIndex.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>', views.IngredientsDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('sandwiches/', views.sandwich_index, name='index'),
]