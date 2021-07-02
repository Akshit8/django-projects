from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('root/', views.api_root),

    path('', include(router.urls)),

    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    # path('snippets/<int:pk>/',
    #      views.SnippetDetail.as_view(), name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/',
    #      views.SnippetHighlight.as_view(), name='snippet-highlight'),

    # path('snippets/v2/', views.SnippetList2.as_view()),
    # path('snippets/v2/<int:pk>/', views.SnippetDetail2.as_view()),

    # path('snippets/v3/', views.SnippetList3.as_view()),
    # path('snippets/v3/<int:pk>/', views.SnippetDetail3.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
