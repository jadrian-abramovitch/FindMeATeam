from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameInfo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django_filters.views import FilterView
from .PostFilter import PostFilter
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)


class GameInfoCreateView(LoginRequiredMixin, CreateView):
	model = GameInfo
	readonly_fields = ['time_Zone']
	fields = ['game', 'positions_played', 'rank', 'server', 'start_Time_Available', 'end_Time_Available', 'in_Game_Name']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

# class GameInfoCreateView(LoginRequiredMixin, CreateView):
# 	form_class = GameInfoForm
# 	template_name = 'game_info/gameinfo_form.html'

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)


class GameInfoListView(FilterView):
	model = GameInfo
	filterset_class = PostFilter
	template_name = 'game_info/home.html'
	ordering = ['-date_posted']
	context_object_name = 'GameInfos'


class GameInfoDetailView(DetailView):
	model = GameInfo
	readonly_fields = ['time_Zone']
	fields = ['game', 'positions_played', 'rank', 'server', 'start_Time_Available', 'end_Time_Available', 'in_Game_Name']

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



