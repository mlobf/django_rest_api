from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Third Part imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializers
from .models import Post


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"name": "john", "age": 23}
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid() 
        serializer.save()
        return Response(serializer.data)


