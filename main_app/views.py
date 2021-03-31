from django.shortcuts import render
from django.http import HttpResponse

from .models import Child
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', { 'children' : children })