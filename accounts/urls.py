from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup2'),

    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success2'),

    path('login/', auth_views.LoginView.as_view(template_name='login2.html'), name='login2'),

    path('logout/', auth_views.LogoutView.as_view(template_name='logout2.html'), name='logout2'),
]