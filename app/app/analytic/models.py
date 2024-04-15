from django.db import models


class Bank(models.Model):
    title = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analytic_banks"

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    banks = models.ManyToManyField(to=Bank, db_table="analytic_report_banks")

    class Meta:
        db_table = "analytic_reports"

    def __str__(self):
        return self.title


class Indicator(models.Model):
    display_types = (
        (0, "Decimal"),
        (1, "Percent"),
    )
    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    display = models.IntegerField(choices=display_types, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        db_table = "analytic_indicators"

    def __str__(self):
        return self.title


class IndicatorValue(models.Model):
    report = models.ForeignKey(to=Report, on_delete=models.CASCADE)
    bank = models.ForeignKey(to=Bank, on_delete=models.CASCADE)
    indicator = models.ForeignKey(to=Indicator, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analytic_indicator_values"

    def __str__(self):
        return f"%s" % self.value


class IndicatorValueView(models.Model):
    id = models.IntegerField(primary_key=True)
    report_bank_id = models.IntegerField()
    title = models.CharField(max_length=255)
    report_id = models.IntegerField()
    actives = models.IntegerField()
    loan_portfolio_total = models.IntegerField()
    reverse_repo_operations = models.IntegerField()
    late_payments_7_sum = models.IntegerField()
    late_payments_7_portfolio = models.FloatField()
    late_payments_30_sum = models.IntegerField()
    late_payments_30_portfolio = models.FloatField()
    late_payments_90_sum = models.IntegerField()
    late_payments_90_portfolio = models.FloatField()
    amount_remuneration = models.IntegerField()
    provision_requirements = models.IntegerField()
    liabilities = models.IntegerField()
    contributions_individuals = models.IntegerField()
    contributions_legal_entities = models.IntegerField()
    equity_on_balance_sheet = models.IntegerField()
    excess_of_income_tax = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytic_indicator_value_view'
