from django.urls import path

from . import views

urlpatterns = [
    path('addDetails', views.addDetails, name="addDetails"),
    path('home', views.home, name="home"),
    path('view', views.view, name="view"),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('edit/update', views.update)
]