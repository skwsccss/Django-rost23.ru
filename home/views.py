from django.core.mail import send_mail
from .forms import FeedBackForm, FeedBackForm1, FeedBackForm2, FeedBackForm3, FeedBackForm4, FeedBackForm5
from rost.settings import base as settings
from django.http import HttpResponseRedirect


def feedback1(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"]
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )


def feedback2(request):
    if request.method == 'POST':
        form = FeedBackForm1(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"]
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )


def feedback3(request):
    if request.method == 'POST':
        form = FeedBackForm2(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"]
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )


def feedback4(request):
    if request.method == 'POST':
        form = FeedBackForm3(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"] + "\n" + \
                      "Записаться на: " + cd["need_product"] + "\n" + \
                      "Назначенное время: " + cd["time"] + " " + cd["date"]
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )


def feedback5(request):
    if request.method == 'POST':
        form = FeedBackForm4(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"] + "\n" + \
                      cd['message']
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )


def feedback6(request):
    if request.method == 'POST':
        form = FeedBackForm5(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Обратный звонок от " + cd['name'] + \
                      "\n Телефон: " + cd["phone"] + "\n" + \
                      cd['email']
            send_mail(
                cd['name'],
                message,
                settings.ADMIN_E_MAIL,
                [settings.ADMIN_E_MAIL],
            )
        return HttpResponseRedirect('/')