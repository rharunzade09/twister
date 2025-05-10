from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.template.defaulttags import comment
from django.views.generic import View
from .models import Post, Likes
from .form import CommentsForm

# Create your views here.
class PostView(View):
    '''Вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    ''' Отдельная страница записи '''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = CommentsForm()
        return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})


class AddComments(View):
    '''Добавление комментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    '''Добавление лайка'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    '''Удаление лайка/дизлайк'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
