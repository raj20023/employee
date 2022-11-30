from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Emp List':'/employee-list/',
		'Emp Detail View':'/employee-detail/<str:pk>/',
		'Emp Create':'/emp-create/',
		'Emp Update':'/emp-update/<str:pk>/',
		'Emp Delete':'/emp-delete/<str:pk>/',
        'Cmp List':'/cmp-list/',
		'Cmp Detail View':'/cmp-detail/<str:pk>/',
		'Cmp Create':'/cmp-create/',
		'Cmp Update':'/cmp-update/<str:pk>/',
		'Cmp Delete':'/cmp-delete/<str:pk>/',
		}

	return Response(api_urls)