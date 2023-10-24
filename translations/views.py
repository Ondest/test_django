from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from translations.models import DictionaryModel


class HomePageView(TemplateView):
    title = "My dictionary"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        data['title'] = self.title
        return data


class AddWordView(CreateView):
    template_name = 'form.html'
    model = DictionaryModel
    fields = ['word_1', 'word_2']


class WordListView(ListView):
    template_name = 'words_list.html'
    model = DictionaryModel
