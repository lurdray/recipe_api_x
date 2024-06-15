
from rest_framework import serializers 
from main.models import *

from django.contrib.auth import get_user_model
User = get_user_model()

class TagSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tag 
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Ingredient 
        fields = "__all__"
  
class RecipeSerializer(serializers.ModelSerializer): 
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta: 
        model = Recipe 
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'account_type']



class GetRecipeSerializer(serializers.ModelSerializer): 
    custom_user = UserSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta: 
        model = Recipe 
        fields = "__all__"


