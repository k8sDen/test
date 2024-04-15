from rest_framework import serializers

from analytic.models import Report, IndicatorValueView


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class IndicatorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorValueView
        fields = '__all__'
