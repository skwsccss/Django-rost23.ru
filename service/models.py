from django.db import models

# Create your models here.
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms
from home.models import CategoryPrice


class AllServicePage(Page):
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
    )
    categories = ParentalManyToManyField('home.CategoryPrice', blank=True, related_name="category_in_price",
                                         verbose_name="Категории цен")

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


class CategoryServicePage(Page):
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
    )
    categories = ParentalManyToManyField('home.CategoryPrice', blank=True, related_name="category_in_category",
                                         verbose_name="Категории цен")

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


class ServicePage(Page):
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
    )
    categories = ParentalManyToManyField('home.CategoryPrice', blank=True, related_name="category_in_service",
                                         verbose_name="Категории цен")

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


