from django import template
from home.models import TestimonialImage
from news.models import NewsPage


register = template.Library()


@register.inclusion_tag('tags/testy-carousel.html', takes_context=True)
def testy_carousel(context):
    items = TestimonialImage.objects.order_by("-date")
    return {'items': items, }


@register.inclusion_tag('tags/testy_in_tab.html', takes_context=True)
def testy_in_tab(context):
    items = TestimonialImage.objects.order_by("-date")
    return {'items': items, }


@register.inclusion_tag('tags/news_at_home.html', takes_context=True)
def news_at_home(context):
    items = NewsPage.objects.order_by("-date")

    return {'items': items,  }