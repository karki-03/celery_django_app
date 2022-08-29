from django.contrib import admin
from django.urls import path, include
from send_mail.views import *

urlpatterns = [
    path("", HomeView.as_view()),
    path("sendmail/", SendMailView.as_view()),
]
