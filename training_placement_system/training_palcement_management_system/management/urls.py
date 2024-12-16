from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.students, name='student'),
    path('companies/', views.companies, name='companies'),
    path('placement/', views.placement, name='placement'),
]
