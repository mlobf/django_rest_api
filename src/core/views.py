from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Third Part imports
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"name": "john", "age": 23}
        return Response(data)




# Create your views here.

"""def test_view(request):
    data = {"name": "john", "age": 23}

    return JsonResponse(data)

    """
