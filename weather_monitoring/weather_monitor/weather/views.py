from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,'main.html')
def index(request):
    return render(request,'index.html')
def style(request):
    return render(request,'style.css')
def script(request):
    return render(request,'script.js')