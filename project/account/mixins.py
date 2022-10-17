from django.shortcuts import redirect


class NormalizeEmailMixin:
    def _normalize_email(self):
        self.data = dict(self.data.items())
        email = self.data.get('email')
        if email is not None:
            self.data['email'] = email.lower()


class NotLoggedRequiredMixin:
    not_logged_required_redirect: str = None

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.not_logged_required_redirect is None:
                self.not_logged_required_redirect = '/'
            return redirect(self.not_logged_required_redirect)
        return super().dispatch(request, *args, **kwargs)
