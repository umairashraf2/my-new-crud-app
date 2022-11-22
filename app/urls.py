from django.contrib import admin
from django.urls import path
from app.views import Home, Login, Signup, Signout, Read, delete, Search

urlpatterns = [
    path("", Home, name="home"),
    path("employee_update/<int:id>/", Home, name="employee_update"),
    path("login/", Login, name="login"),
    path("signup/", Signup),
    path("logout/", Signout),
    path("read/", Read, name="read"),
    path("delete/<int:id>/", delete, name="delete"),
    path("search/", Search, name="delete"),
]
