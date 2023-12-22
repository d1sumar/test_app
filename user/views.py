from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, UpdateView
from pyexpat.errors import messages

from user.forms import LoginForm, RegisterForm
from user.models import User


# Create your views here.

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'pages/login_page.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')

        # form is not valid or user is not authenticated
        # messages.error(request, f'Invalid username or password')
        return render(request, 'pages/login_page.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "pages/register_page.html", {"form": form})

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        return render(request, "pages/register_page.html", {"form": form})


def loguot_view(request):
    logout(request)
    return redirect("home")


class ProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = "pages/profile.html"


class EditProdileView(UpdateView):
    model = User
    fields = ["avatar", "username", "first_name", "last_name", "email"]
    template_name = "pages/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy("user:profile", kwargs={"pk": self.object.pk})


class DeleteProfileView(DeleteView):
    model = User
    template_name = "pages/delete_profile.html"

    def get_success_url(self):
        return reverse_lazy("home")
