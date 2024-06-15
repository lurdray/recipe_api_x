from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
  
from main.models import Recipe
from main.serializers import *
from rest_framework import status


#########################
###############################

@swagger_auto_schema(methods=['POST'], request_body=RecipeSerializer)
@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == "GET":
        recipe = Recipe.objects.all()
        serializer = GetRecipeSerializer(recipe, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        #data = JSONParser().parse(request)
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


    else:
        pass



@swagger_auto_schema(methods=['PUT', "DELETE"], request_body=RecipeSerializer)
@api_view(['GET', 'PUT', "DELETE"])
def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)

    except:
        return JsonResponse({"error": "recipe not found"}, status=400)

    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        #data = JSONParser().parse(request)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == "DELETE":
        recipe.delete()
        return HttpResponse(status=201)


    else:
        pass



@swagger_auto_schema(methods=['POST'], request_body=IngredientSerializer)
@api_view(['POST'])
def add_ingredient_to_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except recipe.DoesNotExist:
        return Response({'error': 'patient not found'}, status=status.HTTP_404_NOT_FOUND)

    ingredient_data = JSONParser().parse(request) 
    ingredient_serializer = IngredientSerializer(data=ingredient_data) 
    if ingredient_serializer.is_valid(): 
        ingredient_serializer.save() 
        ingredient_id = ingredient_serializer.data["id"]
        recipe.ingredients.add(ingredient_id)
        return Response(ingredient_serializer.data, status=status.HTTP_200_OK)
    
    return Response(ingredient_serializer.errors, status=400)



@swagger_auto_schema(methods=['POST'], request_body=TagSerializer)
@api_view(['POST'])
def add_tag_to_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except recipe.DoesNotExist:
        return Response({'error': 'patient not found'}, status=status.HTTP_404_NOT_FOUND)

    tag_data = JSONParser().parse(request) 
    tag_serializer = TagSerializer(data=tag_data) 
    if tag_serializer.is_valid(): 
        tag_serializer.save() 
        tag_id = tag_serializer.data["id"]
        recipe.tags.add(tag_id)
        return Response(tag_serializer.data, status=status.HTTP_200_OK)
    
    return Response(tag_serializer.errors, status=400)




@api_view(['GET'])
def filter_recipes_by_ingredient(request, ingredient):
    if request.method == "GET":

        recipe = Recipe.objects.filter(ingredients__name=ingredient)
        serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    

@api_view(['GET'])
def filter_recipes_by_tag(request, tag):
    if request.method == "GET":

        recipe = Recipe.objects.filter(tags__name=tag)
        serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse(serializer.data, safe=False)
    
      
@api_view(['GET'])
def filter_recipes_by_username(request, username):
    if username:
        custom_user = User.objects.filter(username=username).first()
        if custom_user:
            recipes = Recipe.objects.filter(custom_user=custom_user)
            serializer = RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response({"detail": "Username not provided."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def filter_recipes_by_name(request, name):

    recipe = Recipe.objects.filter(name__icontains=name)
    serializer = RecipeSerializer(recipe, many=True)
    return JsonResponse(serializer.data, safe=False)
    

################################
#########################################

#@api_view(['GET'])
#def recipe(request):
#    if request.method == 'GET':
#        data = {
#            "status": True,
#            "message": "RECIPE API",
#            "status_code": 201,
#        }
#        return Response(data)
    



#@api_view(['POST'])
#def add_recipe(request):
#    if request.method == 'POST':
#        name = request.data["name"]
#        detail = request.data["detail"]
#        ingredients = request.data["ingredients"]
#        tags = request.data["tags"]

#        recipe = Recipe.objects.create(name=name, detail=detail, ingredients=ingredients, tags=tags)
#        recipe.save()
        

#        data = {
#            "status": True,
#            "message": "Add recipe was successful",
#            "status_code": 201,
#            "id": recipe.id
#        }
#        return Response(data)
    


#@api_view(['GET'])
#def all_recipe(request):
#    if request.method == 'GET':

 #       recipes = Recipe.objects.all()

  #      final_recipes = []
   #     for item in recipes:
     #       new_obj = {
    #            "id": item.id,
      #          "name": item.name, 
       #         "detail": item.detail, 
        #        "ingredients": item.ingredients, 
             #   "tags": item.tags, 
            #    }
            
         #