from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return render(request, 'game_info/home.html')
	#return HttpResponse('<h1>Blog Home</h1>')