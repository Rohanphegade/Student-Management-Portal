from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Lead


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

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        if name and len(name.strip()) < 3:
            raise ValidationError("Full name must be at least 3 characters long.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email = email.lower()
            if not email.endswith('@gmail.com'):
                raise ValidationError("Only valid Gmail addresses are allowed (example@gmail.com).")

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        if len(phone) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")
        return phone

    def clean(self):
        cleaned_data = super().clean()

        total_fees = cleaned_data.get('total_fees')
        paid_fees = cleaned_data.get('paid_fees')
        admission_date = cleaned_data.get('admission_date')
        completion_date = cleaned_data.get('completion_date')

        if total_fees is not None and total_fees <= 0:
            raise ValidationError("Total fees must be greater than zero.")

        if paid_fees is not None and paid_fees < 0:
            raise ValidationError("Paid fees cannot be negative.")

        if total_fees is not None and paid_fees is not None:
            if paid_fees > total_fees:
                raise ValidationError("Paid fees cannot be greater than total fees.")

        if admission_date and completion_date:
            if completion_date < admission_date:
                raise ValidationError(
                    "Completion date cannot be earlier than admission date."
                )

        return cleaned_data


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

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        if name and len(name.strip()) < 3:
            raise ValidationError("Full name must be at least 3 characters long.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email = email.lower()
            if not email.endswith('@gmail.com'):
                raise ValidationError("Only valid Gmail addresses are allowed (example@gmail.com).")

        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        if len(phone) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")
        return phone
