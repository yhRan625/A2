from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='login'),
    path('', include('students.urls')), 
]