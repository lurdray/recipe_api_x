# recipe_api_x
Recipe api is a simple rest api built with Django Rest Framework(Python) for Mastering Backend Bootcamp 2.0

This recipe api uses swagger ui:
/swagger/
/redoc/

dependencies:
1. django
2. djangorestframework
3. drf_yasg
4. setuptools

To run on local host

1. git clone https://github.com/lurdray/recipe_api_x.git
2. cd recipe_api_x
3. source venv/bin/activate
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. python3 manage.py runserver
7. go-to localhost:8000/swagger/

