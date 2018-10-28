from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment, AdoptarRescatado
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


    """Metodo Inicio"""

def inicio(request):
    return render(request, 'blog/inicio.html', {})


    """Metodo Adoptar"""
        
def adopta(request):
    adopt = AdoptarRescatado.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/adopta.html', {'adopt':adopt})

def adopta_detail(request, pk):
    adopt = get_object_or_404(AdoptarRescatado, pk=pk)
    return render(request, 'blog/adopta.html', {'adopt': adopt})

def adopta_new(request):
    if request.method == "POST":
        form = AdoptarRescatado(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = AdoptarRescatado()
    return render(request, 'blog/adopta.html', {'form': form})

def adopta_edit(request, pk):
    adopt = get_object_or_404(AdoptarRescatado, pk=pk)
    if request.method == "POST":
        form = AdoptarRescatado(request.POST, instance=adopt)
        if form.is_valid():
            adopt = form.save(commit=False)
            adopt.author = request.user
            adopt.published_date = timezone.now()
            adopt.save()
            return redirect('adopta', pk=adopt.pk)
    else:
        form = AdoptarRescatado(instance=adopt)
    return render(request, 'blog/adopta.html', {'form': form})
    

    """Metodo Contacto"""

def contacto(request):
    return render(request, 'blog/contacto.html', {})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})