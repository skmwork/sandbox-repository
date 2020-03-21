from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from articles.models import Article, Comment


# Create your views here.
def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не нйдена!')

    latest_comments_list = article.comment_set.order_by('-id')

    return render(request, 'articles/detail.html', {'article': article, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не нйдена!')
    article.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))
