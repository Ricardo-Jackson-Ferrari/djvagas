from django.views.generic import TemplateView


class Home(TemplateView):
    extra_context = {'title': 'home'}
    template_name = 'common/home.html'
