from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


def home(request):
     context = { 'posts':Post.objects.all()    }
     return render(request, 'my_space/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'my_space/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7   # here 7 indicates number of post_object that a page will hold

class UserPostListView(ListView):
    model = Post
    template_name = 'my_space/users_posts.html'
    context_object_name = 'posts'
    paginate_by = 7   # here 7 indicates number of post_object that a page will hold


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(DetailView):
    model = Post
    template_name = 'my_space/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    success_url = '/'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'my_space/about.html')


def game(request):
    return render(request, 'my_space/game/games.html')





