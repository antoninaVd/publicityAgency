from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^order/$', views.order, name='order'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^articles/$', views.articles, name='articles'),
]