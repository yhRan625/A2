# Importing the path function from Django's urls module
from django.urls import path
# Importing the views from the students application
from students.views import student_list_view, student_detail_view, student_add_view, student_edit_view

# Defining the URL patterns for the students application
urlpatterns = [
    # The root URL ('') is mapped to the student_list_view
    path('', student_list_view, name='student_list'),
    # The URL 'student/<int:pk>/' is mapped to the student_detail_view. The <int:pk> part is a variable part of the URL that will be passed to the view as a parameter
    path('student/<int:pk>/', student_detail_view, name='student_detail_view'),
    # The URL 'add_student/' is mapped to the student_add_view
    path('add_student/', student_add_view, name='student_add_view'),
    # The URL 'edit_student/<int:pk>/' is mapped to the student_edit_view. The <int:pk> part is a variable part of the URL that will be passed to the view as a parameter
    path('edit_student/<int:pk>/', student_edit_view, name='student_edit_view'),
]