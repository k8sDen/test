import logging

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import permissions, status
from rest_framework.response import Response

from analytic.models import Indicator, IndicatorValue

from analytic.services import ExcelProcessor

logger = logging.getLogger('app')


class ExcelUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.AllowAny]
    columns = [
        'n', 'bank', 'actives', 'loan_portfolio_total',
        'loan_portfolio_including_reverse_repo_operations',
        'from_it_loans_with _late_payments_over_7_days_sum',
        'from_it_loans_with _late_payments_over_7_days_share_in_the_loan_portfolio',
        'from_it_loans_with _late_payments_over_30_days_sum',
        'from_it_loans_with _late_payments_over_30_days_share_in_the_loan_portfolio',
        'from_it_loans_with _late_payments_over_90_days_sum',
        'from_it_loans_with _late_payments_over_90_days_share_in_the_loan_portfolio',
        'amount_of_overdue_loans_including_overdue_remuneration',
        'provisions_formed_for_the_loan_portfolio_in_accordance_with_IFRS_requirements',
        'liabilities', 'of_which_contributions_individuals',
        'of_which_contributions_legal_entities', 'equity_on_balance_sheet',
        'excess_of_current_income_expenses_over_current_expenses_income_after_payment_of_income_tax',
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
            return Response({'detail': 'Файл успешно обработан.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({'error': 'Ошибка при обработке файла.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
