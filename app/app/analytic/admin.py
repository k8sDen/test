from django.contrib import admin

from analytic.models import Report, Bank, Indicator, IndicatorValue


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent_id', 'code', 'display', 'order')
    list_editable = ('code', 'display', 'order')
    list_display_links = ('title',)


@admin.register(IndicatorValue)
class IndicatorValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'indicator', 'value', 'bank')
    list_display_links = ('indicator',)
