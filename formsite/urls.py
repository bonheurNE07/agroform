from django.urls import path
from . import views
urlpatterns = [
    path("", views.home ,name="home"),
    path("agroform/", views.agroform, name="agroform"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    #path('download_excel/', views.agroform, name='download_excel'),
]
