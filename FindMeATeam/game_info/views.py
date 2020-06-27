from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameInfo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)


# Create your views here.

# @login_required
# def home(request):
# 	return render(request, 'game_info/home.html')
	#return HttpResponse('<h1>Blog Home</h1>')

class GameInfoCreateView(LoginRequiredMixin, CreateView):
	model = GameInfo
	fields = ['game', 'positions_played', 'rank', 'server', 'start_Time_Available', 'end_Time_Available']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class GameInfoListView(ListView):
	template_name = 'game_info/home.html'
	model = GameInfo
	ordering = ['-date_posted']
	context_object_name = 'GameInfos'


class GameInfoDetailView(DetailView):
	model = GameInfo
	fields = ['game', 'positions_played', 'rank', 'server', 'start_Time_Available', 'end_Time_Available']

class UserGamesList(ListView):
	model = GameInfo
	context_object_name = 'GameInfos'
	template_name = 'game_info/user_gameinfo_list.html'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return GameInfo.objects.filter(author=user).order_by('-date_posted')


class GameInfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = GameInfo
	fields = ['game', 'positions_played']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class GameInfoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = GameInfo
	success_url = '/game-info/'

	def test_func(self):
		gameInfo = self.get_object()
		if self.request.user == gameInfo.author:
			return True
		else:
			return False



