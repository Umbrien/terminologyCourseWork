from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from utils import term_unicode__icontains

from terminology.models import Term


class Home(TemplateView):  # can be replaced by ListView, but it'll be too pizdato
    template_name = "terminology/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'terms': Term.objects.all()[:50]
        })
        return context


class TermView(DetailView):
    model = Term
    pk_url_kwarg = 'term_pk'
    context_object_name = 'term'
    template_name = 'terminology/term_details.html'

class Search(ListView):
    """Search terms"""
    template_name = 'terminology/search.html'

    def get_queryset(self):
        return Term.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        q = self.request.GET.get('q')

        context['q'] = q

        context.update({
            'terms': term_unicode__icontains(q)
        })
        return context

def save(request):
    q = request.GET.get('q')

    search_set = term_unicode__icontains(q)

    content = serialize('yaml', search_set)
    return HttpResponse(content, content_type='application/json')
