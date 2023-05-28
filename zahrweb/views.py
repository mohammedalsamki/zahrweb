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
    about = About.objects.all()

    context = {
        "poster_image": posters,
        "news": news,
        "number_of_achivments": number_of_achivments,
        "active_projects": active_projects,
    }

    return render(request, "basic.html", context=context)


def detail(request, primary_key):
    news = News.objects.get(pk=primary_key)
    context = {"news": news}
    return render(request, "news_detail.html", context)


class NewsListView(generic.ListView):
    model = News
    news_list = "news_list"  # your own name for the list as a template variable
    template_name = "home/index.html"  # The HTML template for this view

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(NewsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["some_data"] = "This is just some data"
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "zahrweb/news_details.html"

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


def signup(request):
    form = UserCreationForm(request.POST)
    form = SignUpForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("index")
    context = {"form": form}
    return render(request, "signup.html", context)


from .forms import InKindDonationForm, CashDonationForm


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
