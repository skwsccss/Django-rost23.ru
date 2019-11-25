# -*- coding: utf-8 -*-
from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname1",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone1", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))


class FeedBackForm1(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname2",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone2", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))


class FeedBackForm2(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname3",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone3", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))


class FeedBackForm3(forms.Form):
    TIME_LIST = (
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18:30'),
            )
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname4",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone4", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))
    need_product = forms.CharField(max_length=300,
                            widget=forms.TextInput(attrs={"id": "need_product", "class": "form-control",
                            "placeholder": "Имплантация "}))
    time = forms.CharField(widget=forms.Select(attrs={"class": "form-control", "aria-invalid": "false", "id": "ftime4",
                                                      "placeholder": "Время"}, choices=TIME_LIST),required=True)
    date = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control datetime required",
                           "id": "datepicker",
                           "placeholder": "Дата"}),
                           required=True)


class FeedBackForm4(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname5",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone5", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))
    message = forms.CharField(max_length=1000,
                              widget=forms.Textarea(attrs={"id": "fmess5", "class": "form-control", "rows": "3",
                                                           "placeholder": "Ваш отзыв"}))


class FeedBackForm5(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname6",
                           "placeholder": "Ваше имя *"}), max_length=150, required=True)
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={"id": "fmail6",
                                                                           "class": "form-control",
                                                                           "placeholder": "Ваш E-mail *"}))
    phone = forms.CharField(max_length=100, required= True,
                            widget=forms.TextInput(attrs={"id": "fphone6", "class": "form-control required phone",
                            "placeholder": "Телефон *"}))

