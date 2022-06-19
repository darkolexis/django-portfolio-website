from django.urls import path
from cert import views

urlpatterns = [
    path('certifications/',views.certifications,name="certifications"),
]
