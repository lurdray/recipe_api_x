from django.urls import path
from . import views 

app_name = "custom_user"

urlpatterns = [ 

    path("sign-up/", views.sign_up, name="sign_up"),
    path("sign-in/", views.sign_in, name="sign_in"),
    path("all/", views.all, name="all"),
    path("update/<str:user_id>/", views.update_user, name="update_user"),
    path("delete/<str:user_id>/", views.delete_user, name="delete_user"),
    path("get-user-detail/<str:user_id>/", views.get_user_detail, name="get_user_detail"),


] 

