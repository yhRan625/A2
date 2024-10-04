# Importing the StudentForm and SearchForm from forms
from students.forms import StudentForm, SearchForm
# Importing the Student model
from students.models import Student

# Importing necessary modules from Django
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# View for adding a student, requires login
@login_required
def student_add_view(request):
    # If the request method is GET, create an empty form
    if request.method == 'GET':
        form = StudentForm()
    # If the request method is POST, populate the form with the POST data
    else:
        form = StudentForm(request.POST)
        # If the form data is valid
        if form.is_valid():
            # Save the student data and return a student object
            student = form.save()
            # Add a success message
            messages.success(request, 'add Student!')
            # Redirect to the student detail view
            return redirect('student_detail_view', pk=student.pk)
        # If the form data is not valid, add an error message
        else:
            messages.error(request, 'correct the error below.')
    # Render the form page
    return render(request, 'student_form.html', {'form': form})

# View for editing a student, requires login
@login_required
def student_edit_view(request, pk):
    # Get the student object to be edited, if it does not exist, return a 404 error
    student = get_object_or_404(Student, pk=pk)
    # If the request method is GET, populate the form with the student data
    if request.method == 'GET':
        form = StudentForm(instance=student)
    # If the request method is POST, populate the form with the POST data and the student data
    else:
        form = StudentForm(request.POST, instance=student)
        # If the form data is valid
        if form.is_valid():
            # Save the student data and return a student object
            student = form.save()
            # Add a success message
            messages.success(request, 'Student ok!')
            # Redirect to the student detail view
            return redirect('student_detail_view', pk=student.pk)
        # If the form data is not valid, add an error message
        else:
            messages.error(request, 'correct the error below.')
    # Render the form page
    return render(request, 'student_form.html', {'form': form})

# View for listing students, requires login
@login_required
def student_list_view(request):
    # Create a search form and populate it with the GET data
    form = SearchForm(request.GET)
    # Get all student objects
    students_list = Student.objects.all()

    # If the form data is valid
    if form.is_valid():
        # Get the query string
        query = form.cleaned_data.get('query')
        # Filter the student list to only include students whose first name or last name contains the query string
        students_list = students_list.filter(first_name__icontains=query) | students_list.filter(last_name__icontains=query)
    
    # Create a paginator, 1 student per page
    paginator = Paginator(students_list, 1) 
    # Get the page number
    page_number = request.GET.get('page')
    # Get the students for the current page
    students = paginator.get_page(page_number)

    # Render the student list page
    return render(request, 'student_list.html', {'students': students, 'form': form})

# View for displaying a student's details, requires login
@login_required
def student_detail_view(request, pk):
    # Get the student object, if it does not exist, return a 404 error
    student = get_object_or_404(Student, pk=pk)
    # Render the student detail page
    return render(request, 'student_detail.html', {'student': student})