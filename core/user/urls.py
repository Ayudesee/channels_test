from django.urls import path

from user.views import LoginView

urlpatterns = [path('accounts/login', LoginView.as_view())]
