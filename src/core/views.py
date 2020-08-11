from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def test_view(request):
    data = {"name": "john", "age": 23}

    return JsonResponse(data, safe=False)
