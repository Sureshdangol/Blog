from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from blog.models import Profile

from blog.models import Profile
from.forms import SignUpForm,EditProfileForm,PasswordChangingForm


# Create your views here.
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profiles.html"
    fields = ['bio','profile_image','fb_url','twitter_url','website_url','git_url']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name =  'registration/user_profile.html'


    def get_context_data(self, *args, **kwargs):
        #page_user = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
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
