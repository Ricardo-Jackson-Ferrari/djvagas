from faker import Faker
from pytest import fixture

from project.account import facade as account_facade
from project.account.forms import UserSignupForm
from project.roles import Candidate


@fixture
def fake():
    return Faker('pt_BR')


@fixture
def user_candidate(fake):
    def create_user_candidate(self=None):
        data_user = {
            'first_name': fake.name(),
            'email': fake.email(),
            'password1': (
                password := f'{fake.random_number(digits=10)}{fake.first_name()}'
            ),
            'password2': password,
            'role': Candidate.get_name(),
        }
        form = UserSignupForm(data=data_user)

        user = account_facade.create_candidate(form)

        return user

    return create_user_candidate


@fixture
def user_candidate_cls(user_candidate, request):

    request.cls.user_candidate = user_candidate
