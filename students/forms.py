# Importing the Student model
from students.models import Student
# Importing the forms module from Django
from django import forms
# Importing the necessary validators from Django's core validators
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

# Defining the StudentForm, which inherits from Django's ModelForm
class StudentForm(forms.ModelForm):
    # The grade field is an integer field with two validators: it must be larger than 1 and smaller than 12
    grade = forms.IntegerField(
        validators=[
            MinValueValidator(1, message="Grade be larger than 1"),
            MaxValueValidator(12, message="Grade be small 12")
        ]
    )
    # The email field is an email field with a validator that checks if the input is a valid email
    email = forms.EmailField(
        validators=[EmailValidator(message="Enter valid email.")]
    )

    # Meta class for additional form options
    class Meta:
        # The model associated with this form is the Student model
        model = Student
        # The fields included in this form
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

# Defining the SearchForm, which inherits from Django's Form
class SearchForm(forms.Form):
    # The query field is a character field with a label 'Search'
    query = forms.CharField(label='Search')