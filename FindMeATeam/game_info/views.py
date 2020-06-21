from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
	return render(request, 'game_info/home.html')
	#return HttpResponse('<h1>Blog Home</h1>')