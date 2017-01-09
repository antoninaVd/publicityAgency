from django.shortcuts import render

def home(request):
    return render(request, 'publicity_agency/home.html', {})

def order(request):
    return render(request, 'publicity_agency/order.html', {})

def requirements(request):
    return render(request, 'publicity_agency/requirements.html', {})

def contact(request):
    return render(request, 'publicity_agency/contacts.html', {})

def articles(request):
    return render(request, 'publicity_agency/articles.html', {})

def article_item(request):
    return render(request, 'publicity_agency/article-item.html', {})
