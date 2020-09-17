from django import template
from ..models import Category


register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"


@register.inclusion_tag('tem-project/partials/category-navbar.html')
def category_navbar():
    return {
        "category":Category.objects.filter(status=True)
    }