from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, RedirectView, TemplateView
from shortener.forms import LinkForm
from shortener.models import IndexPageText, Link


class IndexView(CreateView):
    template_name = "pages/home.html"
    form_class = LinkForm

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["texts"] = IndexPageText.objects.get()
        return context

    def get_success_url(self):
        return reverse_lazy(
            "shortener:link_detail", kwargs={"url_id": self.object.shortened_url_id}
        )


class AboutView(TemplateView):
    template_name = "pages/about.html"


class LinkDetailView(DetailView):
    template_name = "pages/link_detail.html"
    pk_url_kwarg = "url_id"

    def get_object(self, queryset=None):
        link = get_object_or_404(Link, shortened_url_id=self.kwargs["url_id"])
        return link

    def get_context_data(self, **kwargs):
        context = super(LinkDetailView, self).get_context_data()
        context["texts"] = IndexPageText.objects.get()
        return context


class LinkRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, shortened_url_id=self.kwargs["url_id"])
        link.count += 1
        link.save()
        return link.url
