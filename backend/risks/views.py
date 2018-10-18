# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from .models import Risk_Type, Field, Risk, Field_Risk
from .serializers import RiskTypeSerializer, FieldSerializer, RiskSerializer
from .serializers import FieldRiskSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status


class Pagination(PageNumberPagination):

    # This size is affecting the response for list methods
    page_size = 3

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    pagination_class = Pagination


class FieldRiskViewSet(ModelViewSet):
    queryset = Field_Risk.objects.all()
    serializer_class = FieldRiskSerializer
    pagination_class = Pagination


class RiskTypeViewSet(ModelViewSet):
    queryset = Risk_Type.objects.all()
    serializer_class = RiskTypeSerializer
    pagination_class = Pagination


class RiskViewSet(ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    pagination_class = Pagination

    def create(self, request, *args, **kwargs):
        serializerR = RiskSerializer(data=request.data['risk'],
                                     context={'request': request})
        serializerR.is_valid(raise_exception=True)
        self.perform_create(serializerR)
        headers = self.get_success_headers(serializerR.data)

        for fieldRisk in request.data['fieldRisk']:
            fieldRisk['risk'] = serializerR.data['url']
            serializerFR = FieldRiskSerializer(data=fieldRisk,
                                               context={'request': request})
            serializerFR.is_valid(raise_exception=True)
            self.perform_create(serializerFR)

        return Response(serializerR.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers
                        )

    def retrieve(self, request, pk=None):
        jsonResponse = {}

        querysetR = Risk.objects.all()
        risk = get_object_or_404(querysetR, pk=pk)
        serializerRisk = RiskSerializer(risk, context={'request': request})
        jsonResponse['risk'] = serializerRisk.data

        querysetFR = Field_Risk.objects.all()
        fieldRisks = get_list_or_404(
                                    querysetFR, risk=serializerRisk.data['pk']
                                    )
        serializerFieldRisk = FieldRiskSerializer(
                            fieldRisks, many=True, context={'request': request}
                            )
        jsonResponse['fieldRisk'] = serializerFieldRisk.data
        return Response(jsonResponse)
