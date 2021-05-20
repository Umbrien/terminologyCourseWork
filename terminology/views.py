from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import TemplateView
from django.views.generic import DetailView


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
