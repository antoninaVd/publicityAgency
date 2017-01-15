from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import OrderForm

def home(request):
	articles = Article.objects.filter(date__lte=timezone.now()).order_by('-date')[:2]
	return render(request, 'publicity_agency/home.html', {'articles':articles})

def order(request):
	form=OrderForm(request.POST)
	return render(request, 'publicity_agency/order.html', {'form':form})

def requirements(request):
    return render(request, 'publicity_agency/requirements.html', {})

def contact(request):
	company='no company'
	product='no product'
	design=False
	duration='duration-none'
	contact='no contact'
	tel='123456'
	email='noemail@no.em'
	publicity_type='no_type'

	if request.method == 'POST' :
		form=OrderForm(request.POST)

		if form.is_valid():
			company=form.cleaned_data['company']
			product=form.cleaned_data['product']
			design=form.cleaned_data['design']
			duration=form.cleaned_data['duration']
			contact=form.cleaned_data['contact']
			tel=form.cleaned_data['tel']
			email=form.cleaned_data['email']
			publicity_type=form.cleaned_data['publicity_type']

			try:
				msg_plain = render_to_string('../templates/publicity_agency/email.txt', {'company':company,'product':product,'design':design,'duration':duration,'contact':contact,'tel':tel,'email':email, 'publicity_type':publicity_type})
				msg_html = render_to_string('../templates/publicity_agency/email.html', {'company':company,'product':product,'design':design,'duration':duration,'contact':contact,'tel':tel,'email':email, 'publicity_type':publicity_type})
				msg_plain_client = render_to_string('../templates/publicity_agency/email_client.txt')
				msg_html_client = render_to_string('../templates/publicity_agency/email_client.html')
				send_mail('New order',msg_plain,'PRMonde notification <metrolicite@gmail.com>', ['metrolicite@gmail.com'], html_message=msg_html)
				send_mail('PRMonde order',msg_plain_client,'PRMonde <metrolicite@gmail.com>', [email], html_message=msg_html_client)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return redirect('contact')
	else:
		form=OrderForm()

	return render(request, 'publicity_agency/contacts.html', {'company':company,'product':product,'design':design,'duration':duration,'contact':contact,'tel':tel,'email':email, 'publicity_type':publicity_type})

def articles(request):
	articles = Article.objects.filter(date__lte=timezone.now()).order_by('-date')
	return render(request, 'publicity_agency/articles.html', {'articles' : articles})

def article_item(request, pk):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'publicity_agency/article-item.html', {'article':article})
