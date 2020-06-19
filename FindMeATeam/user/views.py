from django.shortcuts import render, redirect
from .forms import RegisterUserForm

def profile(request):
	return render(request, 'user/profile.html')


def register(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = RegisterUserForm()

	return render(request, 'user/register.html', {'form': form})


