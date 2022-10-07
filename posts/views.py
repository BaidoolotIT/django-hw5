from django.shortcuts import render
from posts.models import Post, Comment
from posts.forms import PostForms, CommentForms
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from posts.constants import PAGINATION_LIMIT


def main(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        start_post = (len(posts) // PAGINATION_LIMIT) * page - 1 if page > 1 else 0
        end_post = start_post + PAGINATION_LIMIT
        count = len(posts) // PAGINATION_LIMIT
        data = {
            "posts": posts[start_post:end_post],
            'pages': range(1, (len(posts) // PAGINATION_LIMIT) + count)
        }

        return render(request, 'posts.html', context=data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post_id=post)
    if request.method == 'GET':
        data = {
            'comment_form': CommentForms,
            'post': post,
            'comments': comments,
        }

        return render(request, 'detail.html', context=data)

    elif request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data.get('author'),
                text=form.cleaned_data.get('text'),
                post_id=id
            )
            return redirect(f'/posts/{id}/')
        else:
            return render(request, 'detail.html', context={
                'comment_form': form,
                'post': post,
                'comments': comments,
                'id': id,
            })


def create_post(request):
    if request.method == 'GET':
        return render(request, 'create_post.html', context={
            'post_form': PostForms})

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                stars=form.cleaned_data.get('stars'),
                type=form.cleaned_data.get('type')
            )
            return redirect(f'/posts/{id}/')
        else:
            return render(request, 'create_post.html', context={
                'post_form': form
            })


def change_post(request, id):
    if request.method == 'GET':
        return render(request, 'change_form.html', context={
            'post_form': PostForms,
            'id': id
        })

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=id)
            post.title = form.data.get('title')
            post.description = form.data.get('description')
            post.stars = form.data.get('stars')
            post.type = form.data.get('type')
            post.save()
            return redirect('/')
        else:
            return render(request, 'change_form.html', context={
                'post_form': form,
                'id': id
            })
