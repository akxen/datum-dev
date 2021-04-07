from django.urls import path, re_path

from . import views

urlpatterns = [
    path('dispatch_scada/', views.DispatchSCADAView.as_view()),
    re_path('dispatch_scada/detail', views.DispatchSCADADetailView.as_view()),

    path('dispatch_report/case_solution/', views.DispatchReportCaseSolutionView.as_view()),
    path('dispatch_report/region_solution/', views.DispatchReportRegionSolutionView.as_view()),
    path('dispatch_report/interconnector_solution/', views.DispatchReportInterconnectorSolutionView.as_view()),
    # path('dispatch_report/constraint_solution/', views.DispatchReportConstraintSolutionView.as_view()),

    # path('p5min/case_solution/', views.P5minCaseSolutionView.as_view()),
    # path('p5min/region_solution/', views.P5minRegionSolutionView.as_view()),
    # path('p5min/interconnector_solution/', views.P5minInterconnectorSolutionView.as_view()),
    # path('p5min/constraint_solution/', views.P5minConstraintSolutionView.as_view()),
]
