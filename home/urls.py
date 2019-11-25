"""khu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views as main

urlpatterns = [
    url(r'^feedback-callback', main.feedback1, name='callback'),
    url(r'^home-place', main.feedback2, name='homeplace'),
    url(r'^header-call', main.feedback3, name='headercall'),
    url(r'^about-form', main.feedback4, name='aboutform'),
    url(r'^message-form', main.feedback5, name='messform'),
    url(r'^menu-form', main.feedback6, name='menuform'),

]

