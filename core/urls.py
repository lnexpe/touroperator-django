from django.urls import path
from django.contrib.auth import views as user_auth
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', user_auth.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', user_auth.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password-reset/',
         user_auth.PasswordResetView.as_view(template_name='core/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         user_auth.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         user_auth.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         user_auth.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
         name='password_reset_complete'),
]
