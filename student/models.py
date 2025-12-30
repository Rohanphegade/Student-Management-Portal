from django.db import models

class Student(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course_name = models.CharField(max_length=100)

    admission_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)

    total_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Fees"
    )

    paid_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Paid Fees"
    )

    remaining_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
        verbose_name="Remaining Fees"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )
    lms_username = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name="LMS Username"
    )

    certificate_id = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name="Certificate ID"
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.remaining_fees = self.total_fees - self.paid_fees
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.full_name} ({self.course_name})"


class Lead(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    college_name = models.CharField(
        max_length=150,
        verbose_name="College Name"
    )

    interested_course = models.CharField(
        max_length=100,
        verbose_name="Interested Course"
    )

    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Notes / Remarks"
    )

    enquiry_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.full_name} - {self.interested_course}"
