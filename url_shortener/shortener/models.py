from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
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


class Link(models.Model):
    url = models.URLField(verbose_name="Real URL")
    shortened_url_id = models.CharField(
        verbose_name="Shortened URL ID", unique=True, editable=False, max_length=8
    )
    count = models.PositiveIntegerField(verbose_name="Click count", default=0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.shortened_url_id:
            self.shortened_url_id = get_random_string(length=8)
        super(Link, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "shortener:link_redirect", kwargs={"url_id": self.shortened_url_id}
        )
