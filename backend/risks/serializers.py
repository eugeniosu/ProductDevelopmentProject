from .models import Risk_Type, Field, Risk, Field_Risk
from rest_framework import serializers


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ('pk', 'name', 'created', 'type', 'url', 'enumValues')


class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk_Type
        fields = ('pk', 'name', 'created', 'field', 'url')


class FieldRiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field_Risk
        fields = ('pk', 'value', 'created', 'field', 'risk')


class RiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk
        fields = ('pk', 'name', 'created', 'risk_type', 'url')
