from django import template
from django.db.models import QuerySet
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/template_tags/drop_down.html')
def drop_down(query: QuerySet):
    context = {}
    if hasattr(query, 'menu_item'):
        query = query.menu_item.all()
    else:
        query = query.child_field.all()
    context['items'] = query
    return context


@register.inclusion_tag('menu/template_tags/menu.html')
def draw_menu(value: QuerySet | str):
    context = {}
    if isinstance(value, str):
        item = MenuItem.objects.prefetch_related(
            'child_field',
        ).filter(named_url=value)
        context['menu'] = item.first()
    else:
        context['menu'] = value
    return context
