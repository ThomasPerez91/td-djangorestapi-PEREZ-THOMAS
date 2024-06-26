from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('researchers/', views.researcher_list, name='researcher_list'),
    path('researcher/<int:pk>/', views.researcher_detail, name='researcher_detail'),
    path('researcher/new/', views.researcher_create, name='researcher_create'),
    path('researcher/<int:pk>/edit/',
         views.researcher_update, name='researcher_update'),
    path('researcher/<int:pk>/delete/',
         views.researcher_delete, name='researcher_delete'),
    path('publications/', views.publication_list, name='publication_list'),
    path('publication/<int:pk>/', views.publication_detail,
         name='publication_detail'),
    path('publication/new/', views.publication_create, name='publication_create'),
    path('publication/<int:pk>/edit/',
         views.publication_update, name='publication_update'),
    path('publication/<int:pk>/delete/',
         views.publication_delete, name='publication_delete'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('search/', views.search, name='search'),
]
