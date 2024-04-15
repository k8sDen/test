from django.urls import path

from analytic.views import ExcelUploadView, ReportsAPIView, IndicatorValueAPIView

urlpatterns = [
    path('upload/', ExcelUploadView.as_view(), name='excel-upload'),
    path('reports/', ReportsAPIView.as_view(), name='reports'),
    path('report/<int:pk>/values/', IndicatorValueAPIView.as_view(), name='indicator-values')
]
