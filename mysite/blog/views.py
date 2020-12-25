#IMPORTS REQUIRED FOR FUNCTION BASED VIEWS
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
#IMPORTS REQUIRED FOR CLASS BASED VIEWS
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
#IMPORT FOR AUTHORIZATIONS
from blog.models import Post,Comment
from django.views.generic import(TemplateView,ListView,
                                 DetailView,CreateView,UpdateView,
                                 DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#CLASS BASED VIEWS:
#(1).Classs Based View For the About Page:
class AboutView(TemplateView):
    template_name = 'about.html'
#(2)View For the Posts:
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        #Python Version Of A SQL QUERRY:
        #The Query below grabs data from the Post model and filters them based on different conditions
        #__lte stands for less then or equal to
        #the -published date attribute is ordered in descending format
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#(3)CBV for Details about a Certain Post
class PostDetailView(DetailView):
    model = Post
#(4)CBV For Creating A new Post
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'        #url for the login Page
    redirect_field_name='blog/post_detail.html'      #redirects the user to the Post Detail Page if He/She is Logged In
    form_class = PostForm
    model = Post
#(5)CBV for Creating Updating A Current Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
#(6)CBV For Deleting A Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
#(7)CBV FOR DRAFT LIST:
class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='/blog/post_list.html'
    model= Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


###############################################
###############################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html',{'form': form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
