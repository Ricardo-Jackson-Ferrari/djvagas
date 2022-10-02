class NormalizeEmailMixin:
    def _normalize_email(self):
        self.data = dict(self.data.items())
        email = self.data.get('email')
        if email is not None:
            self.data['email'] = email.lower()
