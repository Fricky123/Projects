from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Article

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def article_list(request):
    article_list = reversed(Article.objects.all().values())
    
    context = {'article_list': article_list}
    
    template = loader.get_template('articles_page.html')
    
    return HttpResponse(template.render(context, request))

def article_page(request):
    # article_page = Article.objects.all()[index]
    
    # context = {'article page': article_page}
    
    # template = loader.get_template('articles_page_individual.html')
    
    # return HttpResponse(template.render(context, request))
    template = loader.get_template('articles_page_individual).html')
    
    return HttpResponse(template.render(request))
