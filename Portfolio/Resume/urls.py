from django.urls import path
from Resume import views
urlpatterns = [
    path('', views.Home,name='home'),
    path('about',views.About,name='about'),
    path('resume',views.Resume,name='resume'),
    path('contact',views.Contact,name='contact'),
    path('project',views.Project,name='project'),
    path('project1',views.Project1,name='project1'),
    path('education',views.Education,name='education'),
    path('skills',views.Skills,name='skills'),
]