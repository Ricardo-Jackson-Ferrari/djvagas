from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import FormView

from project.account import facade
from project.account.forms import UserSignupForm
from project.account.mixins import NotLoggedRequiredMixin


class AccountCreateView(NotLoggedRequiredMixin, FormView):
    form_class = UserSignupForm
    template_name: str = 'account/create.html'
    success_url = reverse_lazy('account:login')

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()

        facade.user_assign_role(user, form.cleaned_data['role'])

        match form.cleaned_data['role']:
            case 'candidate':
                facade.create_candidate_profile(user)
            case _:
                ...

        return super().form_valid(form)
