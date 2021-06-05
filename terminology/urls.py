from django.urls import path, re_path, include
from .views import Home, TermView, Search


urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    re_path(r'^term/(?P<term_pk>\d+)/', TermView.as_view(), name='term_details'),
    re_path(r'^.?$', Home.as_view(), name='index'),
]
