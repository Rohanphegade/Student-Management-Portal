from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:student_id>/', views.student_documents, name='student_documents'),
    path('student/<int:student_id>/upload/', views.upload_document, name='upload_document'),
    path('delete/<int:doc_id>/', views.delete_document, name='delete_document'),

]

