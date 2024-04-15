import logging

from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from analytic.filters import PrimeFilterBackend, PrimeOrderFilter
from analytic.models import Indicator, IndicatorValue, Report, IndicatorValueView
from analytic.paginations import PrimePagination
from analytic.serializers import ReportSerializer, IndicatorValueSerializer
from analytic.services import ExcelProcessor

logger = logging.getLogger('app')


class ExcelUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.AllowAny]
    columns = [
        'n', 'bank', 'actives', 'loan_portfolio_total',
        'reverse_repo_operations', 'late_payments_7_sum',
        'late_payments_7_portfolio', 'late_payments_30_sum',
        'late_payments_30_portfolio', 'late_payments_90_sum',
        'late_payments_90_portfolio', 'amount_remuneration',
        'provision_requirements', 'liabilities',
        'contributions_individuals', 'contributions_legal_entities',
        'equity_on_balance_sheet', 'excess_of_income_tax',
    ]

    def post(self, request, *args, **kwargs):
        file_path = request.FILES.get('file')
        if not file_path:
            return Response({'detail': 'Пожалуйста, загрузите файл.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            indicators = Indicator.objects.filter(code__in=self.columns).order_by('order').values('id', 'code')
            processor = ExcelProcessor(file_path, self.columns, indicators)
            indicator_values = processor.process_file()
            IndicatorValue.objects.bulk_create(indicator_values, batch_size=500)
            return Response({'detail': 'Файл успешно загружен.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({'error': 'Ошибка при обработке файла.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReportsAPIView(ListAPIView):
    pagination_class = None
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class IndicatorValueAPIView(ListAPIView):
    pagination_class = PrimePagination
    filter_backends = (PrimeOrderFilter, PrimeFilterBackend)
    serializer_class = IndicatorValueSerializer

    def get_queryset(self):
        report_id = self.kwargs.get('pk')
        return IndicatorValueView.objects.filter(
            report_id=report_id
        )
