# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('report/<int:report_id>/', views.report_view, name='report_view'),
]
