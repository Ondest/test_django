from django.urls import path
from .views import HomePageView, AddWordView, WordListView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home/", HomePageView.as_view(), name="home"),
    path("add_word/", AddWordView.as_view(), name="form"),
    path('words_list/', WordListView.as_view(), name='words_list')
]