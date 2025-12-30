from django.db import models
from student.models import Student


class Document(models.Model):

    DOCUMENT_TYPE_CHOICES = [
        ('offer_letter', 'Offer Letter'),
        ('internship_certificate', 'Internship Certificate'),
        ('experience_letter', 'Experience Letter'),
        ('other_certificate', 'Other Certificate'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES
    )

    file = models.FileField(
        upload_to='documents/student_files/'
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return f"{self.student.full_name} - {self.get_document_type_display()}"
