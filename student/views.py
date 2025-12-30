from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm, LeadForm
from .models import Lead
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import permission_required


def student_list(request):
    students = Student.objects.all()

    # Search
    search_query = request.GET.get('q')
    if search_query:
        students = students.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)
        )

    # Filter
    status_filter = request.GET.get('status')
    if status_filter:
        students = students.filter(status=status_filter)

    course_filter = request.GET.get('course')
    if course_filter:
        students = students.filter(course_name__icontains=course_filter)

    # Pagination
    paginator = Paginator(students, 10)  # 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'student/student_list.html', {
        'page_obj': page_obj
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student/student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student/student_form.html', {'form': form})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student/student_detail.html', {
        'student': student
    })

@permission_required('student.delete_student', raise_exception=True)
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student/student_confirm_delete.html', {
        'student': student
    })

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'student/lead_list.html', {'leads': leads})


def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()

    return render(request, 'student/lead_form.html', {'form': form})


def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('lead_list')


def lead_convert_to_student(request, pk):
    lead = get_object_or_404(Lead, pk=pk)

    # Pre-fill student form using lead data
    initial_data = {
        'full_name': lead.full_name,
        'email': lead.email,
        'phone': lead.phone,
        'course_name': lead.interested_course,
    }

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            lead.delete()   # remove lead after conversion
            return redirect('student_list')
    else:
        form = StudentForm(initial=initial_data)

    return render(request, 'student/lead_convert.html', {
        'form': form,
        'lead': lead
    })
