from django.urls import path,include
from Projects import views


urlpatterns = [
    path('projects', views.MyProjects.as_view()),
    path('projects/<slug:slug>', views.ProjectDetails.as_view()),
    path('projectimg/<project_slug>', views.ProjectImages.as_view())

]