from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('post/post_list.html')


# def post_modify(request, post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.created_date = timezone.now()
#             post.save()
#             return redirect('post:post_detail', pk=post_pk)
#     else:
#         form = PostForm(instance=post)
#         context = {
#             'form': form,
#             'posts': post,
#         }
#     return render(request, 'post/post_modify.html', context)

# def post_modify(request, post_pk):
#     # get_object_or_404를 이용해서 Comment객체 가져오기
#     post = get_object_or_404(Post, pk=post_pk)
#     if request.method == 'POST':
#         # Form을 이용해 객체를 update시킴 (data에 포함된 부분만 update됨)
#         form = PostForm(data=request.POST, instance=post)
#         form.save()
#         if next:
#             return redirect(next)
#         return redirect('post:post_detail', post_pk=post.pk)
#     else:
#         # CommentForm에 기존 comment인스턴스의 내용을 채운 bound form
#         form = PostForm(instance=post)
#     context = {
#         'form': form,
#     }
#     return render(request, 'post/comment_modify.html', context)



def post_create(request):
    if request.method == 'POST':
        print()
        form = PostForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            Post.objects.create(
                comment=comment,
                author=request.user,
            )
            return redirect('main')
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'post/post_create.html', context)
