from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel


class NewsIndexPage(Page):
    intro = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(NewsIndexPage, self).get_context(request)
        newspages = self.get_children().live().order_by('-first_published_at')
        page = request.GET.get('page')
        paginator = Paginator(newspages, 5)  # Show 10 blogs per page
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        context['newspages'] = news
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class NewsPage(Page):
    date = models.DateField("Post date")
    name = models.CharField(blank=True, max_length=250)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
        verbose_name="Миниатюра"
    )
    body = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]
    sidebar = RichTextField(editor='tinymce', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('name'),
        ImageChooserPanel('image'),
        FieldPanel('body', classname="full"),
        FieldPanel('sidebar'),
        InlinePanel('related_pages', label="Связанные новости"),
    ]


class NewsRelatedPage(Orderable):
    page = ParentalKey(NewsPage, related_name='related_pages')
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    name = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('name'),
        PageChooserPanel('related_page', "news.NewsPage"),
    ]

    @property
    def link(self):
        if self.related_page:
            return self.related_page.url