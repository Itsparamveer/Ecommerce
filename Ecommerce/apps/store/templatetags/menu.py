from django import template
from apps.store.models import Product, Category
register = template.Library()
@register.inclusion_tag("menu.html")
def menu():
    categories = Category.objects.all()

    return {'categories': categories}

# This is a simple tag that returns the number of products in the database.
