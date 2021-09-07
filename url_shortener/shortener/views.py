from django.views.generic import TemplateView
from shortener.models import IndexPageText


class IndexView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['texts'] = IndexPageText.objects.get()
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'
