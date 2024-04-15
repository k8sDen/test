import json
from datetime import datetime
from decimal import Decimal

from django.conf import settings
from django.db.models import Q
from rest_framework.filters import OrderingFilter, BaseFilterBackend
import pytz


class PrimeOrderFilter(OrderingFilter):
    ordering_param = 'sortField'
    sort_order_param = 'sortOrder'
    query_param = 'lazyEvent'

    def get_ordering(self, request, queryset, view):
        lazy_event = request.query_params.get(self.query_param)
        params = None if not lazy_event else json.loads(lazy_event)
        if params:
            ordering_param = params.get(self.ordering_param)
            asc_or_desc = params.get(self.sort_order_param)
            if ordering_param and asc_or_desc:
                if asc_or_desc == -1:
                    ordering = ['-{}'.format(ordering_param)]
                else:
                    ordering = ['{}'.format(ordering_param)]
                return ordering
        return self.get_default_ordering(view)

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            return queryset.order_by(*ordering)
        return queryset


class PrimeOrderFilter(OrderingFilter):
    ordering_param = 'sortField'
    sort_order_param = 'sortOrder'
    query_param = 'lazyEvent'

    def get_ordering(self, request, queryset, view):
        lazy_event = request.query_params.get(self.query_param)
        params = None if not lazy_event else json.loads(lazy_event)
        if params:
            ordering_param = params.get(self.ordering_param)
            asc_or_desc = params.get(self.sort_order_param)
            if ordering_param and asc_or_desc:
                if asc_or_desc == -1:
                    ordering = ['-{}'.format(ordering_param)]
                else:
                    ordering = ['{}'.format(ordering_param)]
                return ordering
        return self.get_default_ordering(view)

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            return queryset.order_by(*ordering)
        return queryset


class PrimeFilterBackend(BaseFilterBackend):
    AND = "and"
    OR = "or"
    query_param = 'lazyEvent'
    filtering_param = 'filters'
    operator = "operator"
    constraints = "constraints"
    value = "value"
    match_mode = "matchMode"
    starts_with = "startsWith"
    contains = "contains"
    not_contains = "notContains"
    ends_with = "endsWith"
    equals = "equals"
    date_is = "dateIs"
    date_is_not = "dateIsNot"
    date_before = "dateBefore"
    not_equals = "notEquals"
    date_after = "dateAfter"
    lt = "lt"
    lte = "lte"
    gt = "gt"
    gte = "gte"

    def filter_queryset(self, request, queryset, view):
        """
        Return a filtered queryset.
        """
        lazy_event = request.query_params.get(self.query_param)
        params = None if not lazy_event else json.loads(lazy_event)
        if params:
            filter_conditions = params.get(self.filtering_param)
            q_objects = Q()
            if filter_conditions:
                or_conditions = Q()
                and_conditions = Q()
                for (field, options) in filter_conditions.items():
                    operator = options.get(self.operator)
                    constraints = options.get(self.constraints)

                    for constraint in constraints:
                        value = constraint.get(self.value)
                        if value is not None:
                            if isinstance(value, str):
                                value = value.strip()
                            match_mode = constraint.get(self.match_mode)
                            qs = Q()
                            if match_mode == self.starts_with:
                                column = "{}__{}".format(field, 'istartswith')
                                qs = Q(**{column: value})

                            elif match_mode == self.contains:
                                column = "{}__{}".format(field, 'icontains')
                                qs = Q(**{column: value})

                            elif match_mode == self.not_contains:
                                column = "{}__{}".format(field, 'icontains')
                                qs = ~Q(**{column: value})

                            elif match_mode == self.ends_with:
                                column = "{}__{}".format(field, 'iendswith')
                                qs = Q(**{column: value})

                            elif match_mode == self.equals:
                                column = field
                                qs = Q(**{column: value})

                            elif match_mode == self.not_equals:
                                column = field
                                qs = ~Q(**{column: value})

                            elif match_mode == self.lt:
                                column = "{}__{}".format(field, 'lt')
                                qs = Q(**{column: value})

                            elif match_mode == self.lte:
                                column = "{}__{}".format(field, 'lte')
                                qs = Q(**{column: value})

                            elif match_mode == self.gt:
                                column = "{}__{}".format(field, 'gt')
                                qs = Q(**{column: value})

                            elif match_mode == self.gte:
                                column = "{}__{}".format(field, 'gte')
                                qs = Q(**{column: value})

                            elif match_mode == self.date_is:
                                value = pytz.timezone(settings.TIME_ZONE).fromutc(datetime.strptime(value, settings.DATETIME_INPUT_FORMATS[2])).strftime('%Y-%m-%d')
                                column = field
                                qs = Q(**{column: value})

                            elif match_mode == self.date_is_not:
                                value = pytz.timezone(settings.TIME_ZONE).fromutc(datetime.strptime(value, settings.DATETIME_INPUT_FORMATS[2])).strftime('%Y-%m-%d')
                                column = field
                                qs = ~Q(**{column: value})

                            elif match_mode == self.date_before:
                                value = pytz.timezone(settings.TIME_ZONE).fromutc(datetime.strptime(value, settings.DATETIME_INPUT_FORMATS[2])).strftime('%Y-%m-%d')
                                column = "{}__{}".format(field, 'lt')
                                qs = Q(**{column: value})

                            elif match_mode == self.date_after:
                                value = pytz.timezone(settings.TIME_ZONE).fromutc(datetime.strptime(value, settings.DATETIME_INPUT_FORMATS[2])).strftime('%Y-%m-%d')
                                column = "{}__{}".format(field, 'gt')
                                qs = Q(**{column: value})
                            if str(operator).lower() == self.AND:
                                and_conditions &= qs
                            elif str(operator).lower() == self.OR:
                                or_conditions |= qs
                if and_conditions:
                    q_objects &= and_conditions

                if or_conditions:
                    q_objects &= or_conditions
            if q_objects:
                return queryset.filter(q_objects)
        return queryset
