from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article

def home(request):
    return render(request, 'publicity_agency/home.html', {})

def order(request):
    return render(request, 'publicity_agency/order.html', {})

def requirements(request):
    return render(request, 'publicity_agency/requirements.html', {})

def contact(request):
    return render(request, 'publicity_agency/contacts.html', {})

def articles(request):
	articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')
	return render(request, 'publicity_agency/articles.html', {'articles' : articles})

def article_item(request, pk):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'publicity_agency/article-item.html', {'article':article})
