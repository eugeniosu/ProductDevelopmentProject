# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Field(models.Model):
    """ This table groups 'Enum_Value' Table and 'Field_Type' table. The idea
    behind this is to reduce the developing time of this prototype.

    'enumValues' and 'type' fields should be part of a separate table each.
    """
    name = models.CharField(
                    max_length=100, blank=True, default='', unique=True
                    )
    # just used when type is 'enum'. The input values must be split by comma
    enumValues = models.CharField(max_length=250, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    choices = (("enum", "enum"),
               ("text", "text"),
               ("date", "date"),
               ("number", "number")
               )
    type = models.CharField(max_length=255,
                            choices=choices)

    def get_name(self):
        """only for testing purposes"""
        return ('name: ' + self.name + ', enumValues: ' + self.enumValues
                + ', type: ' + self.get_type_display())


class Risk_Type(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    field = models.ManyToManyField(Field)

    def get_name(self):
        """only for testing purposes"""
        return 'name: ' + self.name


class Risk(models.Model):
    """This table will store the entries for insurances"""
    name = models.CharField(
                        max_length=100, blank=True, default='', unique=True
                        )
    created = models.DateTimeField(auto_now_add=True)
    risk_type = models.ForeignKey(Risk_Type, on_delete=models.CASCADE)

    def get_name(self):
        """only for testing purposes"""
        return 'name: ' + self.name


class Field_Risk(models.Model):
    value = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)

    def get_value(self):
        """only for testing purposes"""
        return 'value: ' + self.value
