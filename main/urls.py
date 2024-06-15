from django.urls import path
from . import views 

app_name = "main"

urlpatterns = [ 
    #path("recipe/", views.recipe, name="recipe"),
    #path("add-recipe/", views.add_recipe, name="add_recipe"),
    #path("all-recipe/", views.all_recipe, name="all_recipe"),
    #path("delete-recipe/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    #path("update-recipe/<int:recipe_id>/", views.update_recipe, name="update_recipe"),
    #path("search-by-name/<str:name>/recipe/", views.search_by_name_recipe, name="search_by_name_recipe"),

    path("recipe-list/", views.recipe_list, name="recipe_list"),
    path("recipe/<str:recipe_id>/", views.recipe, name="recipe"),

    path('add-ingredient-to-recipe/<str:recipe_id>/', views.add_ingredient_to_recipe, name='add_ingredient_to_recipe'),
    path('add-tag-to-recipe/<str:recipe_id>/', views.add_tag_to_recipe, name='add_tag_to_recipe'),

    path("filter-recipes-by-tag/<str:tag>/", views.filter_recipes_by_tag, name="filter_recipes_by_tag"),
    path("filter-recipes-by-ingredient/<str:ingredient>/", views.filter_recipes_by_ingredient, name="filter_recipes_by_ingredient"),
    path("filter-recipes-by-username/<str:username>/", views.filter_recipes_by_username, name="filter_recipes_by_username"),
    path("filter-recipes-by-name/<str:name>/", views.filter_recipes_by_name, name="filter_recipes_by_name"),
    
] 


