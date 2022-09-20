from django.shortcuts import render
from django.views.generic import View


class Home(View):
    def get(self, request):
        ctx = {}
        ctx['title'] = 'Home'
        return render(self.request, 'common/home.html', ctx)
