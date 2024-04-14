from django.urls import path

from analytic.views import ExcelUploadView

urlpatterns = [
    path('upload/', ExcelUploadView.as_view(), name='excel-upload'),
]
