from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('sandwiches/', views.sandwich_index, name='index'),
    path('sandwiches/<int:sandwich_id>/', views.sandwich_detail, name='detail'),
    path('sandwiches/<int:pk>/update/', views.SandwichUpdate.as_view(), name='sandwich_update'),
    path('sandwiches/<int:pk>/delete/', views.SandwichDelete.as_view(), name='sandwich_delete'),
    path('sandwiches/<int:sandwich_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('ingredients/', views.IngredientsIndex.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>', views.IngredientsDetail.as_view(), name='ingredients_detail'),

]