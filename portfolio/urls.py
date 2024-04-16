from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('skills',views.skills,name='skills'),
    path('experience',views.experience,name='experience'),
    path('projects',views.projects,name='projects'),    
]
