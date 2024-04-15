import logging

import pandas as pd

from analytic.models import Report, Bank, IndicatorValue

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
            report = Report.objects.create(title=sheet_name)
            df = pd.read_excel(
                xls,
                sheet_name=sheet_name,
                engine='xlrd',
                skiprows=6,
                header=0,
                usecols=[x for x in range(0, len(self.columns))],
            )
            # вставляем новые хэдеры
            df.columns = self.columns
            # преобразовываем на %
            df['late_payments_7_portfolio'] *= 100
            df['late_payments_30_portfolio'] *= 100
            df['late_payments_90_portfolio'] *= 100
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
            report.banks.add(bank)
            for indicator in indicators:
                if pd.isna(row.get(indicator['code'], None)):
                    continue
                value = row[indicator['code']]
                indicator_values.append(
                    IndicatorValue(
                        report_id=report.id,
                        bank_id=bank.id,
                        indicator_id=indicator['id'],
                        value=value
                    )
                )
