from django.contrib import admin
from solo.admin import SingletonModelAdmin

from url_shortener.shortener.models import IndexPageText, Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ["shortened_url_id", "count"]


admin.site.register(IndexPageText, SingletonModelAdmin)
