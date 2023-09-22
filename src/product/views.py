from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request


# Create your views here.


@api_view(["GET"])
def get_lesson(request: Request, name: str) -> JsonResponse:
    pass