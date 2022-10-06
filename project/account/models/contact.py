from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.phone

    def clean(self):
        if self.user.contact_set.exclude(pk=self.pk).count() >= 2:
            raise ValidationError(
                _('maximum number of phones already registered')
            )

    def unique_error_message(self, model_class, unique_check):
        error = super().unique_error_message(model_class, unique_check)

        error.message = _('%(phone)s already registered for this user.')
        error.params['phone'] = self.phone

        return error

    class Meta:
        verbose_name = _('contact')
        unique_together = ['user', 'phone']
