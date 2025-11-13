from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("id")
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "course"]
    ordering_fields = ["id", "name", "age"]


def test_view(request):
    return HttpResponse("Hello World - It works!")