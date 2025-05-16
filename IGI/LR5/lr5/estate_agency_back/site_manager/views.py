from django.http import Http404
from django.shortcuts import render

from .models import AboutCompany, FAQ
from articles.models import Article


# Create your views here.
def home(request):
    last_article = Article.objects.last()
    if not last_article:
        last_article = ""
    return render(request, "site_manager/home.html",
    {"article": last_article})


def about(request):
    company = AboutCompany.objects.last()
    if not company:
        return Http404("There is no info about company")
    return render(request, "site_manager/about.html",
    {"company": company})

def news(request):
    return render(request, 'site_manager/news.html')


def faq(request):
    faq = FAQ.objects.all()
    return render(request, 'site_manager/faq.html',
    {"faq": faq})


def contacts(request):
    return render(request, 'site_manager/contacts.html')


def privacy_policy(request):
    return render(request, 'site_manager/privacy_policy.html')


def vacancies(request):
    return render(request, 'site_manager/vacancy.html')