from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
#def home(request):
 #   return  render(request,'home.html',{})
from blog.models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = [-'id']
    ordering = ['-post_date']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'details.html'


class AddPostView(CreateView):
    model = Post
    form_class =PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ['title','title_tag','body']



class DeletePostView(DeleteView):
    model = Post
    template_name ="delete_post.html"
    success_url = reverse_lazy('home')