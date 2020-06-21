from django.shortcuts import render, redirect
from .forms import RegisterUserForm, UpdateUserForm

def profile(request):
	if request.method == "POST":
		form = UpdateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = UpdateUserForm(instance=request.user)

	context = {
		'form': form,
	}
	return render(request, 'user/profile.html', context)
	##return render(request, 'user/profile.html')


def register(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = RegisterUserForm()

	return render(request, 'user/register.html', {'form': form})


