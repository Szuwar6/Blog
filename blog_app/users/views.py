from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormMixin

from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from users.models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Dear {username}, you have been successfully singed up!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile's been updated!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(
        request,
        "users/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")




class UpdateProfile(LoginRequiredMixin,UpdateView):
    user_form = UserUpdateForm
    profile_form = ProfileUpdateForm
    template_name = "users/profile.html"

    def get(self, request):
        user_form = self.user_form(instance=request.user)
        profile_form = self.profile_form(instance=request.user.profile)
        return render(
            request,
            "users/profile.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(request.POST, instance=request.user)
        profile_form = self.profile_form(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile's been updated!")
            return redirect("profile")






