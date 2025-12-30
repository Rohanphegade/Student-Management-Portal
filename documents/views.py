from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm
from student.models import Student


def student_documents(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    documents = student.documents.all()

    return render(request, 'documents/student_documents.html', {
        'student': student,
        'documents': documents
    })


def upload_document(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.student = student
            document.save()
            return redirect('student_documents', student_id=student.id)
    else:
        form = DocumentForm()

    return render(request, 'documents/upload_document.html', {
        'form': form,
        'student': student
    })

def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    student_id = document.student.id

    if request.method == 'POST':
        document.file.delete(save=False)  # delete file from storage
        document.delete()                 # delete DB record
        return redirect('student_documents', student_id=student_id)

    return render(request, 'documents/delete_document.html', {
        'document': document
    })
