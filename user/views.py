from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from user import forms as user_form
from user import models as user_models
from user.forms import ProfileForm

USER = get_user_model()

# UserCreateView
class UserCreateView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = user_form.UserRegisterform
    success_url = reverse_lazy("user:user_login")


class UserLoginView(views.View):
    form_class = auth_forms.AuthenticationForm
    success_url = reverse_lazy("core:home")
    template_name = "registration/login.html"

    def get(self, request):
        context = {
            "form": self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request=request)
        # if form.is_valid():
        form.is_valid()
        username = request.POST.get("username")
        password = request.POST.get("password")
        # to check whether the given username and password are exists or not
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # to login user
            login(request, user)
            messages.success(request, "Successfully Logged in!")
            return redirect(self.success_url)
        messages.error(request, "Login Failed")
        context = {"form": form}
        return render(request, self.template_name, context)


class UserLogoutView(views.View):
    template_name = "registration/logged_out.html"

    def get(self, request):
        logout(request)
        messages.success(request, "Successfully Logged out")
        return render(request, self.template_name)


# profile create view
class ProfileCreateView(views.CreateView):
    template_name = "user/profile_create.html"
    model = user_models.ProfileModel
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile_detail")


# feedback updateview
class ProfileUpdateView(views.UpdateView):
    template_name = "user/profile_update.html"
    model = user_models.ProfileModel
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile_detail")
    extra_context = {"address_form": user_form.AddressForm}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        try:
            address = self.request.user.profilemodel.address.all()
        except:
            address = None
        kwargs.update({"request": self.request, "initial": {"address": address}})
        return kwargs


class ProfileDetailView(views.TemplateView):
    template_name = "user/profile_detail.html"
    model = user_models.ProfileModel
    context_object_name = "profile"


# Address
class AddressCreateView(LoginRequiredMixin, views.FormView):
    template_name = "core/address/address_create.html"
    form_class = user_form.AddressForm

    def form_valid(self, form):
        address = form.save()
        self.request.user.profilemodel.address.add(address)
        messages.success(self.request, message="Address created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        url = self.request.META.get("HTTP_REFERER", "/")
        return url
