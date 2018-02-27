from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.notes_list, name='notes_list'),
]
