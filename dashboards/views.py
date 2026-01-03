from django.shortcuts import render
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from student.models import Student, Lead
from documents.models import Document
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
    permission_required,
)
from accounts.utils import is_admin_or_manager

@login_required
@user_passes_test(is_admin_or_manager)
def dashboard_home(request):
    # 1. Counts for Cards
    total_students = Student.objects.count()
    total_leads = Lead.objects.count()
    total_documents = Document.objects.count()
    
    # 2. Fees Data (Derived from Student model)
    fees_data = Student.objects.aggregate(
        total=Sum('total_fees'),
        paid=Sum('paid_fees'),
        pending=Sum('remaining_fees')
    )
    # Handle None values if no students exist
    total_fees = fees_data['total'] or 0
    paid_fees = fees_data['paid'] or 0
    pending_fees = fees_data['pending'] or 0

    # 3. Charts Data
    
    # Monthly Admissions (Bar Chart)
    # Group students by month of admission_date
    monthly_admissions = Student.objects.annotate(
        month=TruncMonth('admission_date')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    # Prepare data for Chart.js
    admission_labels = []
    admission_data = []
    for entry in monthly_admissions:
        if entry['month']:
            admission_labels.append(entry['month'].strftime('%b %Y'))
            admission_data.append(entry['count'])

    # Student Status Distribution (Pie Chart) - Active vs Completed
    status_counts = Student.objects.filter(status__in=['active', 'completed']).values('status').annotate(
        count=Count('id')
    )
    
    # Convert to dictionary for easy lookup
    counts_dict = {item['status']: item['count'] for item in status_counts}

    # Ensure both Active and Completed are always present
    status_labels = ['Active', 'Completed']
    status_data = [
        counts_dict.get('active', 0),
        counts_dict.get('completed', 0)
    ]
        
    context = {
        'total_students': total_students,
        'total_leads': total_leads,
        'total_documents': total_documents,
        'total_fees': total_fees,
        'paid_fees': paid_fees,
        'pending_fees': pending_fees,
        'admission_labels': admission_labels,
        'admission_data': admission_data,
        'status_labels': status_labels,
        'status_data': status_data,
    }

    return render(request, 'dashboard/home.html', context)

@login_required
@user_passes_test(is_admin_or_manager)
def document_list(request):
    documents = Document.objects.all().select_related('student')
    context = {'documents': documents}
    return render(request, 'dashboard/documents_list.html', context)

@login_required
@user_passes_test(is_admin_or_manager)
def account_list(request):
    # Determine fees data per student
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'dashboard/account_list.html', context)
