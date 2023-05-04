from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('sandwiches/', views.sandwich_index, name='index'),
    path('sandwiches/<int:sandwich_id>/', views.sandwich_detail, name='detail'),
    path('sandwiches/create/', views.SandwichCreate.as_view(), name='sandwiches_create'),
    path('sandwiches/<int:pk>/update/', views.SandwichUpdate.as_view(), name='sandwich_update'),
    path('sandwiches/<int:pk>/delete/', views.SandwichDelete.as_view(), name='sandwich_delete'),
    path('sandwiches/<int:sandwich_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('ingredients/', views.IngredientsIndex.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>', views.IngredientsDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete', views.IngredientDelete.as_view(), name='ingredients_delete'),
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
]