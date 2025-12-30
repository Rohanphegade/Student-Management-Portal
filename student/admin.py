from django.contrib import admin
from .models import Student, Lead


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'course_name',
        'lms_username',
        'total_fees',
        'paid_fees',
        'remaining_fees',
        'certificate_id',
        'status',
    )

    list_filter = ('status', 'course_name')
    search_fields = ('full_name', 'email', 'phone')

    fieldsets = (
        ("Basic Information", {
            'fields': ('full_name', 'email', 'phone')
        }),
        ("Course Details", {
            'fields': ('course_name', 'admission_date', 'completion_date', 'status')
        }),
        ("Fees Information", {
            'fields': ('total_fees', 'paid_fees')
        }),
        ("LMS & Certification", {
            'fields': ('lms_username', 'certificate_id')
        }),
    )



@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'college_name',
        'interested_course',
        'status',
        'enquiry_date',
    )

    list_filter = ('status', 'interested_course', 'college_name')
    search_fields = ('full_name', 'email', 'phone', 'college_name')

