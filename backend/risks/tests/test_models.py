from django.test import TestCase
from risks.models import Field, Risk_Type, Risk, Field_Risk
import pytest


@pytest.mark.django_db
class ModelTest(TestCase):
    """ Test all models and its relations """

    def setUp(self):
        fieldEnum = Field.objects.create(
            name='fieldEnumType',
            enumValues='value1, value2',
            type='enum')
        fieldText = Field.objects.create(
            name='fieldTextType', type='text')
        fieldDate = Field.objects.create(
            name='fieldDateType', type='date')
        fieldNumber = Field.objects.create(
            name='fieldNumberType', type='number')
        riskType = Risk_Type.objects.create(
            name='RiskTypeTest')
        riskType.field.add(fieldEnum, fieldText, fieldDate, fieldNumber)
        risk = Risk.objects.create(
            name='RiskTest', risk_type=riskType)
        Field_Risk.objects.create(
            value='value2', risk=risk, field=fieldEnum)
        Field_Risk.objects.create(
            value='Greetings from Chile', risk=risk, field=fieldText)
        Field_Risk.objects.create(
            value='2018-01-01', risk=risk, field=fieldDate)
        Field_Risk.objects.create(
            value='988777123', risk=risk, field=fieldNumber)

    def test_field_enum_added(self):
        """ Check if the field type enum was added """
        field_enum_type = Field.objects.get(name='fieldEnumType')
        self.assertEqual(
            field_enum_type.get_name(),
            "name: fieldEnumType, enumValues: value1, value2, type: enum"
            )

    def test_field_text_added(self):
        """ Check if the field type text was added """
        field_text_type = Field.objects.get(name='fieldTextType')
        self.assertEqual(
            field_text_type.get_name(),
            "name: fieldTextType, enumValues: , type: text"
            )

    def test_field_date_added(self):
        """ Check if the field type date was added """
        field_date_type = Field.objects.get(name='fieldDateType')
        self.assertEqual(
           field_date_type.get_name(),
           "name: fieldDateType, enumValues: , type: date"
           )

    def test_field_number_added(self):
        """ Check if the field type number was added """
        field_number_type = Field.objects.get(name='fieldNumberType')
        self.assertEqual(
           field_number_type.get_name(),
           "name: fieldNumberType, enumValues: , type: number"
           )

    """ Test module for RiskType model """
    def test_risk_type_added(self):
        """ Check if a new record was correctly saved """
        field_risk_type = Risk_Type.objects.get(name='RiskTypeTest')
        self.assertEqual(
            field_risk_type.get_name(), "name: RiskTypeTest")

    def test_risk_type_count(self):
        """ Check if all fields were added (many to one) """
        field_risk_type = Risk_Type.objects.get(name='RiskTypeTest')
        self.assertEqual(4, field_risk_type.field.count())

    """ Test module for Risk model """
    def test_risk_added(self):
        """ Check if a new record was correctly saved """
        field_risk_type = Risk.objects.get(name='RiskTest')
        self.assertEqual(
            field_risk_type.get_name(), "name: RiskTest")

    """ Test module for Field_Risk model """
    def test_field_risk_added(self):
        field_field_risk = Field_Risk.objects.get(value='Greetings from Chile')
        self.assertEqual(
            field_field_risk.get_value(), "value: Greetings from Chile")
