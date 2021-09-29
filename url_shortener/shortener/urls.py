from django.urls import path

from url_shortener.shortener.views import (
    AboutView,
    IndexView,
    LinkDetailView,
    LinkRedirectView,
)

app_name = "shortener"
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("link/<str:url_id>/", LinkDetailView.as_view(), name="link_detail"),
    path("<str:url_id>/", LinkRedirectView.as_view(), name="link_redirect"),
]
