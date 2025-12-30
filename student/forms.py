from django import forms
from .models import Student
from .models import Lead

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'email',
            'phone',
            'lms_username',
            'course_name',
            'admission_date',
            'completion_date',
            'total_fees',
            'paid_fees',
            'certificate_id',
            'status',
        ]


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'full_name',
            'email',
            'phone',
            'college_name',
            'interested_course',
            'status',
            'notes',
        ]


