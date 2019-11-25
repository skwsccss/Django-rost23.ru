from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.wagtailsnippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms


class HomePage(Page):
    open_text = RichTextField(editor='tinymce', help_text="Открытая часть текста",
                              blank=True, verbose_name="Видимый текст")
    hidden_text = RichTextField(editor='tinymce', help_text="Часть текста, открывающаяся скриптом",
                              blank=True, verbose_name="Скрытый текст")

    content_panels = Page.content_panels + [
        FieldPanel('open_text', classname="full"),
        FieldPanel('hidden_text', classname="full"),
        InlinePanel('slider_images', label="Изображения для слайдера"),
    ]


class HomeSliderImage(Orderable):
    page = ParentalKey(HomePage, related_name='slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изображение"
    )
    h2_name = models.CharField(blank=True, max_length=250)
    h3_name = models.CharField(blank=True, max_length=250)
    slogan = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('h2_name'),
        FieldPanel('h3_name'),
        FieldPanel('slogan'),
    ]


class AboutPage(Page):
    text_col1 = RichTextField(editor='tinymce', help_text="Текст в первой колонке",
                              blank=True, verbose_name="Текст 1")
    text_col2 = RichTextField(editor='tinymce', help_text="Текст во второй колонке",
                              blank=True, verbose_name="Текст 2")
    point1 = RichTextField(editor='tinymce', help_text="Наши преимущества - текст в первой ячейке",
                           blank=True, verbose_name="Преимущества1")
    point2 = RichTextField(editor='tinymce', help_text="Наши преимущества - текст во второй ячейке",
                           blank=True, verbose_name="Преимущества2")
    point3 = RichTextField(editor='tinymce', help_text="Наши преимущества - текст в третьей ячейке",
                           blank=True, verbose_name="Преимущества3")
    point4 = RichTextField(editor='tinymce', help_text="Наши преимущества - текст в четвёртой ячейке",
                           blank=True, verbose_name="Преимущества4")
    point5 = RichTextField(editor='tinymce', help_text="Наши преимущества - текст в пятой ячейке",
                           blank=True, verbose_name="Преимущества5")

    content_panels = Page.content_panels + [
        FieldPanel('text_col1', classname="full"),
        FieldPanel('text_col2', classname="full"),
        FieldPanel('point1', classname="full"),
        FieldPanel('point2', classname="full"),
        FieldPanel('point3', classname="full"),
        FieldPanel('point4', classname="full"),
        FieldPanel('point5', classname="full"),
        InlinePanel('about_slider_images', label="Изображения для слайдера"),
    ]


class AboutSliderImage(Orderable):
    page = ParentalKey(AboutPage, related_name='about_slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изображение"
    )
    ANIMATION_OF_BLOCK = (
        ('bounce', 'bounce'),
        ('flash', 'flash'),
        ('pulse', 'pulse'),
        ('rubberBand', 'rubberBand'),
        ('shake', 'shake'),
        ('headShake', 'headShake'),
        ('swing', 'swing'),
        ('tada', 'tada'),
        ('wobble', 'wobble'),
        ('jello', 'jello'),
        ('bounceIn', 'bounceIn'),
        ('bounceInDown', 'bounceInDown'),
        ('bounceInLeft', 'bounceInLeft'),
        ('bounceInRight', 'bounceInRight'),
        ('bounceInUp', 'bounceInUp'),
        ('bounceOut', 'bounceOut'),
        ('bounceOutDown', 'bounceOutDown'),
        ('bounceOutLeft', 'bounceOutLeft'),
        ('bounceOutRight', 'bounceOutRight'),
        ('bounceOutUp', 'bounceOutUp'),
        ('fadeIn', 'fadeIn'),
        ('fadeInDown', 'fadeInDown'),
        ('fadeInDownBig', 'fadeInDownBig'),
        ('fadeInLeft', 'fadeInLeft'),
        ('fadeInLeftBig', 'fadeInLeftBig'),
        ('fadeInRight', 'fadeInRight'),
        ('fadeInRightBig', 'fadeInRightBig'),
        ('fadeInUp', 'fadeInUp'),
        ('fadeInUpBig', 'fadeInUpBig'),
        ('fadeOut', 'fadeOut'),
        ('fadeOutDown', 'fadeOutDown'),
        ('fadeOutDownBig', 'fadeOutDownBig'),
        ('fadeOutLeft', 'fadeOutLeft'),
        ('fadeOutLeftBig', 'fadeOutLeftBig'),
        ('fadeOutRight', 'fadeOutRight'),
        ('fadeOutRightBig', 'fadeOutRightBig'),
        ('fadeOutUp', 'fadeOutUp'),
        ('fadeOutUpBig', 'fadeOutUpBig'),
        ('flipInX', 'flipInX'),
        ('flipInY', 'flipInY'),
        ('flipOutX', 'flipOutX'),
        ('flipOutY', 'flipOutY'),
        ('lightSpeedIn', 'lightSpeedIn'),
        ('lightSpeedOut', 'lightSpeedOut'),
        ('rotateIn', 'rotateIn'),
        ('rotateInDownLeft', 'rotateInDownLeft'),
        ('rotateInDownRight', 'rotateInDownRight'),
        ('rotateInUpLeft', 'rotateInUpLeft'),
        ('rotateInUpRight', 'rotateInUpRight'),
        ('rotateOut', 'rotateOut'),
        ('rotateOutDownLeft', 'rotateOutDownLeft'),
        ('rotateOutDownRight', 'rotateOutDownRight'),
        ('rotateOutUpLeft', 'rotateOutUpLeft'),
        ('rotateOutUpRight', 'rotateOutUpRight'),
        ('hinge', 'hinge'),
        ('jackInTheBox', 'jackInTheBox'),
        ('rollIn', 'rollIn'),
        ('rollOut', 'rollOut'),
        ('zoomIn', 'zoomIn'),
        ('zoomInDown', 'zoomInDown'),
        ('zoomInLeft', 'zoomInLeft'),
        ('zoomInRight', 'zoomInRight'),
        ('zoomInUp', 'zoomInUp'),
        ('zoomOut', 'zoomOut'),
        ('zoomOutDown', 'zoomOutDown'),
        ('zoomOutLeft', 'zoomOutLeft'),
        ('zoomOutRight', 'zoomOutRight'),
        ('zoomOutUp', 'zoomOutUp'),
        ('slideInDown', 'slideInDown'),
        ('slideInLeft', 'slideInLeft'),
        ('slideInRight', 'slideInRight'),
        ('slideInUp', 'slideInUp'),
        ('slideOutDown', 'slideOutDown'),
        ('slideOutLeft', 'slideOutLeft'),
        ('slideOutRight', 'slideOutRight'),
        ('slideOutUp', 'slideOutUp'),

    )
    block_animation = models.CharField(blank=True, max_length=250,
                                       choices=ANIMATION_OF_BLOCK, verbose_name="Анимация блока",
                                       help_text="Выбрать вид анимации, который будет применён к блоку")
    block_is_animated = models.BooleanField(default= True, help_text="Добавить к блоку класс animated?",
                                            verbose_name="Animated?")
    block_is_infinite = models.BooleanField(default=False, help_text="Добавить к блоку класс infinite?",
                                            verbose_name="infinite?")
    h1_name = models.CharField(blank=True, max_length=250)
    h1_animation = models.CharField(blank=True, max_length=250,
                                       choices=ANIMATION_OF_BLOCK, verbose_name="Анимация h1",
                                       help_text="Выбрать вид анимации, который будет применён к h1")
    h1_is_animated = models.BooleanField(default=True, help_text="Добавить к h1 класс animated?",
                                            verbose_name="Animated h1?")
    h1_is_infinite = models.BooleanField(default=False, help_text="Добавить к h1 класс infinite?",
                                            verbose_name="infinite h1?")
    h3_name = models.CharField(blank=True, max_length=250)
    h3_animation = models.CharField(blank=True, max_length=250,
                                    choices=ANIMATION_OF_BLOCK, verbose_name="Анимация h3",
                                    help_text="Выбрать вид анимации, который будет применён к h3")
    h3_is_animated = models.BooleanField(default=True, help_text="Добавить к h3 класс animated?",
                                         verbose_name="Animated h3?")
    h3_is_infinite = models.BooleanField(default=False, help_text="Добавить к h3 класс infinite?",
                                         verbose_name="infinite h3?")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('block_animation'),
        FieldPanel('block_is_animated'),
        FieldPanel('block_is_infinite'),
        FieldPanel('h1_name'),
        FieldPanel('h1_animation'),
        FieldPanel('h1_is_animated'),
        FieldPanel('h1_is_infinite'),
        FieldPanel('h3_name'),
        FieldPanel('h3_animation'),
        FieldPanel('h3_is_animated'),
        FieldPanel('h3_is_infinite'),

    ]


class WorkPage(Page):
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(WorkPage, self).get_context(request)
        our_works = WorkListImage.objects.all()
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(our_works, 5)  # Show 5 blogs per page
        try:
            works = paginator.page(page)
        except PageNotAnInteger:
            works = paginator.page(1)
        except EmptyPage:
            works = paginator.page(paginator.num_pages)
        context['work_page_images'] = works
        return context

    content_panels = Page.content_panels + [
        InlinePanel('work_page_images', label="Изображения для работ"),
    ]


class WorkListImage(Orderable):
    page = ParentalKey(WorkPage, related_name='work_page_images')
    image1 = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изобр. 1"
    )
    image2 = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изобр. 2"
    )
    h3_name = models.CharField(blank=True, max_length=250)
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")

    panels = [
        ImageChooserPanel('image1'),
        ImageChooserPanel('image2'),
        FieldPanel('h3_name'),
        FieldPanel('text'),
    ]


class ContactPage(Page):
    pass


@register_snippet
class ListPrice(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Цены'


@register_snippet
class CategoryPrice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    items = models.ManyToManyField(ListPrice, related_name="price_list", verbose_name="Список цен")

    panels = [
        FieldPanel('name'),
        FieldPanel('slogan'),
        FieldPanel('items', widget=forms.CheckboxSelectMultiple)
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории цен'


class PricePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
    )
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")
    categories = ParentalManyToManyField('CategoryPrice', blank=True, related_name="category_in")

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


class SpecialistIndexPage(Page):
    pass


class SpecialistPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True,
    )
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ф.И.О.")
    profession = models.CharField(max_length=255, blank=True, null=True, verbose_name="Профессия")
    experience = models.CharField(max_length=255, blank=True, null=True, verbose_name="Стаж работы")
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('name', classname="full"),
        FieldPanel('profession', classname="full"),
        FieldPanel('experience', classname="full"),
        FieldPanel('text', classname="full"),
        InlinePanel('sertificates', label="Сертификаты"),
    ]


class SpecialistList(Orderable):
    page = ParentalKey(SpecialistPage, related_name='sertificates')
    sertificate = models.CharField(max_length=555, blank=True, null=True, verbose_name="Сертификат")
    sertificate_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изображение сертификата", blank=True, null=True,
    )

    panels = [
        FieldPanel('sertificate'),
        ImageChooserPanel('sertificate_image'),
    ]


class TestimonialsPage(Page):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(TestimonialsPage, self).get_context(request)
        testimonials = TestimonialImage.objects.order_by("-date")
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(testimonials, 9)  # Show 9 blogs per page
        try:
            testimonial = paginator.page(page)
        except PageNotAnInteger:
            testimonial = paginator.page(1)
        except EmptyPage:
            testimonial = paginator.page(paginator.num_pages)
        context['testimonial_images'] = testimonial
        return context
    content_panels = Page.content_panels + [
        InlinePanel('testimonial_images', label="Отзывы"),
    ]


class TestimonialImage(Orderable):
    page = ParentalKey(TestimonialsPage, related_name='testimonial_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
        verbose_name="Изображение"
    )
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ф.И.О.")
    date = models.DateField("Post date")
    text = RichTextField(editor='tinymce', blank=True, verbose_name="Текст")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('name'),
        FieldPanel('date'),
        FieldPanel('text'),
    ]

