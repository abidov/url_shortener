from django.db import models
from solo.models import SingletonModel


class IndexPageText(SingletonModel):
    under_form_text = models.TextField(verbose_name="Text under the form")
    after_form_text_title1 = models.CharField(
        verbose_name="First text title after the form", max_length=255
    )
    after_form_text_title2 = models.CharField(
        verbose_name="Second text title after the form", max_length=255
    )
    after_form_text_description1 = models.TextField(
        verbose_name="First text description after the form"
    )
    after_form_text_description2 = models.TextField(
        verbose_name="Second text description after the form"
    )
    copyright_text = models.TextField(verbose_name="Copyright text")

    def __str__(self):
        return "Index Page Texts"

    class Meta:
        verbose_name = "Index Page Texts"
