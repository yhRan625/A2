# Importing the models module from Django's db
from django.db import models

# Defining the Student model
class Student(models.Model):
    # The enrollment_date field is a date field
    enrollment_date = models.DateField()
    # The grade field is an integer field
    grade = models.IntegerField()
    # The first_name field is a character field with a maximum length of 100
    first_name = models.CharField(max_length=100)
    # The last_name field is a character field with a maximum length of 100
    last_name = models.CharField(max_length=100)
    # The email field is an email field
    email = models.EmailField()
    # The date_of_birth field is a date field
    date_of_birth = models.DateField()