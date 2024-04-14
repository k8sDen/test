import logging

import pandas as pd

from analytic.models import Report, Bank, IndicatorValue
from django.shortcuts import get_object_or_404

logger = logging.getLogger('app')


class ExcelProcessor:
    def __init__(self, file, columns, indicators):
        self.file = file
        self.columns = columns
        self.indicators = indicators

    def process_file(self):
        try:
            xls = pd.ExcelFile(self.file)
            return self.process_excel_file(xls)
        except Exception as e:
            logger.error(f"Ошибка при обработке файла: {e}")
            raise

    def process_excel_file(self, xls):
        indicator_values = []
        for sheet_name in xls.sheet_names:
            report = get_object_or_404(Report, code=sheet_name)
            if not report:
                raise
            df = pd.read_excel(xls, sheet_name=sheet_name, engine='xlrd', skiprows=6, header=0, usecols=[x for x in range(0, len(self.columns))])
            df.columns = self.columns
            self.process_dataframe(df, report, self.indicators, indicator_values)
        return indicator_values

    def read_sheet(self, xls, sheet_name):
        try:
            return pd.read_excel(xls, sheet_name=sheet_name, engine='xlrd', skiprows=6, usecols=self.columns)
        except Exception as e:
            error_msg = f"Ошибка при чтении листа {sheet_name}: {str(e)}"
            logger.error(error_msg)
            return pd.DataFrame()

    @staticmethod
    def process_dataframe(df, report, indicators, indicator_values):
        for index, row in df.iterrows():
            if pd.isna(row['n']):
                break
            bank, _ = Bank.objects.get_or_create(title=row['bank'])
            for indicator in indicators:
                if pd.isna(row.get(indicator['code'], None)):
                    continue
                indicator_values.append(
                    IndicatorValue(
                        report_id=report.id,
                        bank_id=bank.id,
                        indicator_id=indicator['id'],
                        value=row[indicator['code']]
                    )
                )
