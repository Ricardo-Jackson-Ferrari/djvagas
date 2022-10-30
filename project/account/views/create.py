from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import FormView

from project.account import facade
from project.account.forms import UserSignupForm
from project.account.mixins import NotLoggedRequiredMixin
from project.roles import Candidate, Company


class Roles:
    candidate = Candidate.get_name()
    company = Company.get_name()


class AccountCreateView(NotLoggedRequiredMixin, FormView):
    form_class = UserSignupForm
    template_name = 'account/create.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        match form.cleaned_data['role']:
            case Roles.candidate:
                facade.create_candidate(form)
            case Roles.company:
                facade.create_company(form)
            case _:
                return HttpResponseBadRequest('role invalid')

        return super().form_valid(form)
