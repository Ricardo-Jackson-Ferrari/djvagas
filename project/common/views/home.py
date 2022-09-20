from django.views.generic import View
from django.shortcuts import render


class Home(View):
    def get(self, request):
        ctx = {}
        ctx['title'] = 'Home'
        return render(self.request, 'common/home.html', ctx)