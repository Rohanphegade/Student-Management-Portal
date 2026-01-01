from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('documents/', views.document_list, name='dashboard_documents'),
    path('accounts/', views.account_list, name='dashboard_accounts'),
]
