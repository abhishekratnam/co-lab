from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def index(request):
    return render(request, 'user_profile/profile.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'user_profile/profile.html'
    paginate_by = 3
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'user_profile/post_detail.html'

def post_detail(request, slug):
    template_name = 'user_profile/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name,{'post':post,
                                          'comments':comments,
                                          'new_comment':new_comment,
                                          'comment_form':comment_form})
