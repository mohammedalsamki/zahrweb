from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.my_view, name="about"),
    # path("signup/", views.signup, name="signup"),
    path("news_detail/<int:primary_key>", views.detail, name="news_detail"),
    path(
        "project_detail/<int:primary_key>", views.project_detail, name="project_detail"
    ),
    path("inkinddonation/", views.in_kind_donation, name="inkinddonation"),
    path("cashdonation/", views.Cash_donation, name="cashdonation"),
    path("idea/", views.Idea, name="idea"),
    path("accounts/", include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
