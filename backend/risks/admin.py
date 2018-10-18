# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Field, Risk_Type, Risk, Field_Risk

admin.site.register(Field)
admin.site.register(Risk_Type)
admin.site.register(Risk)
admin.site.register(Field_Risk)
