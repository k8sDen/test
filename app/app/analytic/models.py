from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    code = models.CharField(unique=True, max_length=255)
    unit = models.CharField(max_length=255, default="тыс.тенге")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analytic_reports"

    def __str__(self):
        return self.title


class Bank(models.Model):
    title = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analytic_banks"

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
