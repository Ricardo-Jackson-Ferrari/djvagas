from faker import Faker
from pytest import fixture

from project.account import facade as account_facade
from project.account.forms import UserSignupForm
from project.roles import Candidate, Company


@fixture
def fake():
    return Faker('pt_BR')


@fixture()
def user_form(fake):
    def create_form(role):
        data_user = {
            'first_name': fake.name(),
            'email': fake.email(),
            'password1': (
                password := f'{fake.random_number(digits=10)}{fake.first_name()}'
            ),
            'password2': password,
            'role': role.get_name(),
        }
        form = UserSignupForm(data=data_user)
        return form

    return create_form


@fixture
def user_candidate(user_form):
    def create_user_candidate(self=None):
        user = account_facade.create_candidate(user_form(Candidate))

        return user

    return create_user_candidate


@fixture
def user_candidate_cls(user_candidate, request):

    request.cls.user_candidate = user_candidate
