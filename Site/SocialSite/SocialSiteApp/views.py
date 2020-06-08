#import Modules
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegesterForm, UseUpdateForm, ProfileUpdateForm, UsePicUpdateForm, ContactUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User



# Create views here.
#Home view
@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


#listing Viewsin Home
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def users(request):
    context = {
        'posts': Post.objects.all(),
        'num_post': Post.objects.filter(author=request.user).count()
    }
    return render(request, 'user_post.html', context)

class UserPostListView(ListView):
    model = Post
    template_name = 'user_post.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username',))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username',))
        context['num_post'] = Post.objects.filter(author=user).order_by('-date_posted').count()
        return context

    


#View For Delats view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


#View For Creating post view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#View For update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'author']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#View For Delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/home'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#login view
@login_required
def explore(request):
    return render(request, 'explore.html')



#profile view
@login_required
def profile(request):
    user = request.user
    context = {
        'post':Post.objects.filter(author=request.user).order_by('-date_posted'),
        'user': user,
        'num_post': Post.objects.filter(author=request.user).count()
    }
    return render(request, 'profile.html', context)




#regester view
def regester(request):
    if request.method == 'POST':
        form = UserRegesterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegesterForm()
    return render(request, 'regester.html', {'form': form})



#setting view
@login_required
def settings(request):
    if request.method == 'POST':
        u_form = UseUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        pic_form = UsePicUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        con_form = ContactUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pic_form.is_valid() and u_form.is_valid() and pic_form.is_valid() and con_form.is_valid():
            pic_form.save()
            u_form.save()
            p_form.save()
            con_form.save()
            return redirect('profile')

    else:
        u_form = UseUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        pic_form = UsePicUpdateForm(instance=request.user.profile)
        con_form = ContactUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pic_form': pic_form,
        'con_form': con_form
    }
    return render(request, 'settings.html', context)