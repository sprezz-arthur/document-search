from django.views.generic import ListView
from haystack.generic_views import SearchView
from .search_indexes import TenderIndex


class TenderSearchView(SearchView):
    template_name = "search.html"
    queryset = TenderIndex().search()
