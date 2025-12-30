from django.urls import path
from . import views

urlpatterns = [
    # Student URLs
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_add'),
    path('edit/<int:pk>/', views.student_update, name='student_edit'),
    path('<int:student_id>/view/', views.student_detail, name='student_view'),
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),

    # Lead URLs
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/add/', views.lead_create, name='lead_add'),
    path('leads/delete/<int:pk>/', views.lead_delete, name='lead_delete'),
    path('leads/convert/<int:pk>/', views.lead_convert_to_student, name='lead_convert'),

]
