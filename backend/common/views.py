from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'pageSize'