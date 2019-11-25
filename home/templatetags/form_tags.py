from django import template
from home.forms import FeedBackForm, FeedBackForm1, FeedBackForm2, FeedBackForm3, FeedBackForm4, FeedBackForm5


register = template.Library()


@register.inclusion_tag('tags/feedback1.html', takes_context=True)
def feedback1(context):
    form = FeedBackForm
    return {'form': form, }


@register.inclusion_tag('tags/feedback2.html', takes_context=True)
def feedback2(context):
    form = FeedBackForm1
    return {'form1': form, }


@register.inclusion_tag('tags/feedback3.html', takes_context=True)
def feedback3(context):
    form = FeedBackForm2
    return {'form2': form, }


@register.inclusion_tag('tags/feedback4.html', takes_context=True)
def feedback4(context):
    form = FeedBackForm3
    return {'form3': form, }


@register.inclusion_tag('tags/feedback5.html', takes_context=True)
def feedback5(context):
    form = FeedBackForm4
    return {'form4': form, }


@register.inclusion_tag('tags/feedback6.html', takes_context=True)
def feedback6(context):
    form = FeedBackForm5
    return {'form5': form, }


