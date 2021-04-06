from django.urls import path, re_path

from .views import DispatchSCADALatestView, DispatchSCADADetailView

urlpatterns = [
    path('latest/', DispatchSCADALatestView.as_view()),
    re_path('detail', DispatchSCADADetailView.as_view()),
]
