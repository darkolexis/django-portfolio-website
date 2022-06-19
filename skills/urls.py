from django.urls import path
from skills import views

urlpatterns = [
    path('myskills/',views.myskills,name="myskills"),
]
