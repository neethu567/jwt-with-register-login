from myapp import views
from django.urls import path

urlpatterns = [
    path("sample/", views.sample.as_view(), name="sampletext"),
    path("register/",views.Register.as_view(),name="register"),
    path("login/",views.Login.as_view(),name="Login"),
    path("welcome/",views.Welcome.as_view(),name="welcome"),
    # path("register/",views.Register.as_view(),name="Register")
]
