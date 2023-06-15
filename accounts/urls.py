from django.contrib.auth.views import LoginView
from django.urls import include, path
from accounts.forms import UserLoginForm

urlpatterns =[
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('',include('django.contrib.auth.urls'))
]
