from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import CustomRegistrationForm
from .models import AboutCompany, FAQ, PrivacyPolicy, Vacancy, Contacts
from articles.models import Article
from estate_agency.models import Employee, User, Owner, Customer



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


def faq(request):
    faq = FAQ.objects.all()
    return render(request, 'site_manager/faq.html',
    {"faq": faq})


def contacts(request):
    employees = Contacts.objects.all()
    return render(request, 'site_manager/contacts.html',
                  {"contacts": employees})


def privacy_policy(request):
    policy = PrivacyPolicy.objects.last()
    if not policy: policy = ""
    return render(request, 'site_manager/privacy_policy.html',
                  {"privacy": policy})


def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'site_manager/vacancy.html',
                  {"vacancies" : vacancies})


def register(request):
    message = ""
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
        else:
            message = "Form is not valid!"
    else:
        form = CustomRegistrationForm()
    return render(request, "form.html",
                  {"form": form, "message": message})


def logout(request):
    auth_logout(request)
    return redirect("home")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html",
                  {"form": form})


def profile(request):
    user = User.objects.get(user=request.user)
    employee = Employee.objects.filter(user=user).first()
    owner = Owner.objects.filter(user=user).first()
    customer = Customer.objects.filter(user=user).first()
    return render(request, 'site_manager/profile.html',
                  { "employee": employee,
                            "owner": owner,
                            "customer": customer})