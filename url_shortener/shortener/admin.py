from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import IndexPageText

admin.site.register(IndexPageText, SingletonModelAdmin)
