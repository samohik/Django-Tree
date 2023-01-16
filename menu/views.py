from django.views.generic import TemplateView, DetailView
from menu.models import *


class TreeMenuView(TemplateView):
    template_name = 'menu/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.prefetch_related('menu_item').all()
        return context


class TreeDetailView(DetailView):
    template_name = 'menu/home.html'
    model = MenuItem
    context_object_name = 'menu'

    def get_object(self, queryset=None):
        named_url = self.kwargs.get('named_url')
        query = self.model.objects.prefetch_related(
            'child_field',
        ).filter(named_url=named_url)
        return query


class TestView(TemplateView):
    template_name = 'menu/test.html'



