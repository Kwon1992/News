from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.displayList, name='display_news_lists'),
]