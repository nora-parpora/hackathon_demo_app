from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import pagination

def get_user_from_access_token_in_django_rest_framework_simplejwt(access_token_str):
    access_token_obj = AccessToken(access_token_str)
    user_id=access_token_obj['user_id']
    user=User.objects.get(id=user_id)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50