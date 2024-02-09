from django.urls import path
from .views import DoctorSignUpView, DoctorLoginView, CustomUserSignUpView, CustomUserLoginView


urlpatterns = [
    path('admin/signup/', DoctorSignUpView.as_view(), name='doctor_signup'),
    path('admin/login/', DoctorLoginView.as_view(), name='doctor_login'),
    path('user/signup/', CustomUserSignUpView.as_view(), name='customuser_signup'),
    path('user/login/', CustomUserLoginView.as_view(), name='customuser_login'),

]