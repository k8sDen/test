import json

from rest_framework.pagination import LimitOffsetPagination, _positive_int


class PrimePagination(LimitOffsetPagination):
    limit_query_param = 'rows'
    offset_query_param = 'first'
    query_param = 'lazyEvent'
    limit = 0
    offset = 0
    count = 0
    request = None

    def get_limit(self, request):
        if self.limit_query_param:
            lazy_event = request.query_params.get(self.query_param)
            params = None if not lazy_event else json.loads(lazy_event)
            if params:
                return _positive_int(
                    params.get(self.limit_query_param, self.default_limit),
                    strict=True,
                    cutoff=self.max_limit
                )

        return self.default_limit

    def get_offset(self, request):
        lazy_event = request.query_params.get(self.query_param)
        params = None if not lazy_event else json.loads(lazy_event)
        if params:
            return _positive_int(
                params.get(self.offset_query_param, 0),
            )
        return 0

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])
