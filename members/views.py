from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from.forms import SignUpForm,EditProfileForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_sucess')


def password_sucess(request):
    return render(request,'registration/password_sucess.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
