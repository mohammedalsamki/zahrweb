from django.shortcuts import render
from .models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    Achivment,
    ExistingProjects,
    About,
)
from audioop import reverse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse


# Create your views here.
def index(request):
    posters = poster.objects.all().order_by("-id")[:5]
    news = News.objects.order_by("-date")[:3]
    number_of_achivments = Achivment.objects.all()
    active_projects = ExistingProjects.objects.order_by("-start_date")[:3]

    context = {
        "poster_image": posters,
        "news": news,
        "number_of_achivments": number_of_achivments,
        "active_projects": active_projects,
    }

    return render(request, "index.html", context=context)


def detail(request, primary_key):
    news = News.objects.get(pk=primary_key)
    context = {"news": news}
    return render(request, "news_detail.html", context)


def project_detail(request, primary_key):
    project = ExistingProjects.objects.get(pk=primary_key)
    context = {"projects": project}
    return render(request, "project_detail.html", context)


def about(request):
    abouts = About.objects.all()
    context = {"abouts": abouts}
    return render(request, "about.html", context)


class NewsListView(generic.ListView):
    model = News
    news_list = "news_list"  # your own name for the list as a template variable
    template_name = "index.html"  # The HTML template for this view

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(NewsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["some_data"] = "This is just some data"
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "zahrweb/news_detail.html"

    def news_detail_view(request, primary_key):
        try:
            news = News.objects.get(pk=primary_key)
        except News.DoesNotExist:
            raise Http404("News does not exist")

        return render(request, context={"news": news})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


# def signup(request):
#     form = UserCreationForm(request.POST)
#     form = SignUpForm(request.POST)

#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect("index")
#     context = {"form": form}
#     return render(request, "signup.html", context)
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


from .forms import InKindDonationForm, CashDonationForm, IdeaForm


def in_kind_donation(request):
    if request.method == "POST":
        form = InKindDonationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = InKindDonationForm()
    return render(request, "in_kind_donation.html", {"form": form})


def Cash_donation(request):
    if request.method == "POST":
        form = CashDonationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = CashDonationForm()
    return render(request, "cash_donation.html", {"form": form})


def Idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = IdeaForm()
    return render(request, "idea.html", {"form": form})
