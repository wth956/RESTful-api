from django.shortcuts import render

# from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, format=None):
        data_payload = {
        'name':'Dylan',
        'age':'26'
        }
        return Response(data_payload)

# def TestView(arg):
#     data = {
#         'name':'Dylan',
#         'age':'26'
#     }
#     return JsonResponse(data)