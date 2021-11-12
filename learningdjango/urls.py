"""learningdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def register(self):
    return HttpResponse("This is a registration page...")


def login(self):
    return HttpResponse("Oya login")


def list_natives(self):
    return HttpResponse("All natives")


def delete_a_native(self):
    return HttpResponse("This native has been deleted")


def update_a_native(self):
    return HttpResponse("This native has been updated")


def list_of_cohorts(self):
    return HttpResponse("This is the list of all cohorts")


def create_a_cohort(self):
    return HttpResponse("We just created this cohort")


def update_a_cohort(self):
    return HttpResponse("We just updated this cohort")


def delete_a_cohort(self):
    return HttpResponse("We just deleted this cohort")


def home(self):
    return HttpResponse("This is the home page")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('natives/register', register),
    path('natives/login', login),
    path('natives/', list_natives),
    path('natives/delete', delete_a_native),
    path('natives/update', update_a_native),
    path('cohorts/', list_of_cohorts),
    path('cohorts/create', create_a_cohort),
    path('cohorts/update', update_a_cohort),
    path('cohorts/delete', delete_a_cohort),
    path('', home),
]
