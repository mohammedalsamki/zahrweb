from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.index, name="about"),
    path("signup/", views.signup, name="signup"),
    path("news_detail/<int:pk>", views.detail, name="news_detail"),
    path("inkinddonation/", views.in_kind_donation, name="inkinddonation"),
    path("cashdonation/", views.Cash_donation, name="cashdonation"),
    path("accounts/", include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
