from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('about/',views.aboutpage,name="aboutpage"),
    path('contacts/',views.contactpage,name="contactpage"),
    path('therapy/',views.therapypage,name="therapypage"),
    path('nurse/',views.nursepage,name="nursepage"),
    path('specialists/',views.specialistpage,name="specialistpage"),
    path('inpatients/',views.inpatientpage,name="inpatientpage"),
    path('outpatients/',views.outpatientpage,name="outpatientpage"),
    path('services/',views.servicepage,name="servicespage"),
]
