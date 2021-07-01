from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.SnippetList.as_view()),
    path('v2/', views.SnippetList2.as_view()),
    path('v3/', views.SnippetList3.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    path('v2/<int:pk>/', views.SnippetDetail2.as_view()),
    path('v3/<int:pk>/', views.SnippetDetail3.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
