""" This module contains accounts related URLs and the associates them with the appropriate views """

from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

from accounts.forms import MySetPasswordForm, MyAuthenticationForm

from accounts.views import SpecialUserView

app_name = 'accounts'

urlpatterns = [
    path('users/me/',
         SpecialUserView.as_view()
         ),
    path('password/reset/confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/registration/my_password_reset_confirm.html',
             success_url=reverse_lazy('accounts:password_reset_complete'),
             form_class=MySetPasswordForm,
         ),
         name='password_reset_confirm'),
    path('password/reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/registration/my_password_reset_complete.html',
         ),
         name='password_reset_complete'),
    path('login/',
         auth_views.LoginView.as_view(
            template_name='accounts/registration/login.html',
            authentication_form=MyAuthenticationForm,
            redirect_authenticated_user=True
         ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
