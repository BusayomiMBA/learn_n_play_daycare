from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('children/', views.children_index, name='children'),
    path('children/<int:child_id>/', views.children_show, name='children_show'),
    path('children/create/', views.ChildCreate.as_view(), name='children_create'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='children_update'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='children_delete'),
    path('children/<int:pk>/add_dailyActivities/', views.add_dailyActivities, name='add_dailyActivities'),
]