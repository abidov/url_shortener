from django.urls import path
from .views import IndexView, AboutView

app_name = "shortener"
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
]
