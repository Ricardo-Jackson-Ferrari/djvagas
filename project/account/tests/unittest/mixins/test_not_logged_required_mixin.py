from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.test import TestCase
from model_bakery import baker

from project.account.mixins import NotLoggedRequiredMixin


class NotLoggedRequiredMixinUnittest(TestCase):
    def test_dispatch_redirect_to_root(self):
        request = HttpRequest()
        request.user = baker.make(get_user_model())

        mixin = NotLoggedRequiredMixin()
        mixin.request = request

        resp = mixin.dispatch(request=request)

        self.assertEqual('/', resp.url)

    def test_dispatch_redirect_to_specific_url(self):
        request = HttpRequest()
        request.user = baker.make(get_user_model())

        mixin = NotLoggedRequiredMixin()
        mixin.not_logged_required_redirect = 'another/'
        mixin.request = request

        resp = mixin.dispatch(request=request)

        self.assertEqual('another/', resp.url)

    def test_dispatch_status_code_302(self):
        request = HttpRequest()
        request.user = baker.make(get_user_model())

        mixin = NotLoggedRequiredMixin()
        mixin.request = request

        resp = mixin.dispatch(request=request)

        self.assertEqual(302, resp.status_code)

    def test_dispatch_raise_super(self):
        request = HttpRequest()
        request.user = AnonymousUser()

        mixin = NotLoggedRequiredMixin()
        mixin.request = request

        self.assertRaisesMessage(
            AttributeError,
            "'super' object has no attribute 'dispatch'",
            mixin.dispatch,
            request=request,
        )
