from django.urls import path, re_path

from . import views

urlpatterns = [
    path('dispatch_scada/', views.DispatchSCADAView.as_view()),
    re_path('dispatch_scada/detail', views.DispatchSCADADetailView.as_view()),

    path('dispatch_report/case_solution/', views.DispatchReportCaseSolutionView.as_view()),
    path('dispatch_report/region_solution/', views.DispatchReportRegionSolutionView.as_view()),
    path('dispatch_report/interconnector_solution/', views.DispatchReportInterconnectorSolutionView.as_view()),
    path('dispatch_report/constraint_solution/', views.DispatchReportConstraintSolutionView.as_view()),

    path('p5/case_solution/', views.P5CaseSolutionView.as_view()),
    path('p5/region_solution/', views.P5RegionSolutionView.as_view()),
    path('p5/interconnector_solution/', views.P5InterconnectorSolutionView.as_view()),
    path('p5/constraint_solution/', views.P5ConstraintSolutionView.as_view()),
]
