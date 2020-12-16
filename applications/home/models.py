from django.db import models

# Create your models here.

from model_utils.models import TimeStampedModel

class Suscriber(TimeStampedModel):
    

    email = models.EmailField("email")

    class Meta:

        verbose_name = 'Suscriber'
        verbose_name_plural = 'Suscribers'

    def __str__(self):
        return self.email

