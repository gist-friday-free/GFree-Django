from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('', views.api_root),

    path('running/', views.ServerRunning.as_view(), name='server-running'),

    path('class/', views.ClassList.as_view(), name='class-list'),
    path('class/<int:pk>', views.ClassDetail.as_view(), name='class-detail'),
    # 해당 클래스를 수강하고있는 유저들을 가져오는 것
    path('class/<int:pk>/users', views.ClassDetailUsers.as_view(), name='class-users'),
    path('class/<int:pk>/reviews', views.ClassDetailReviews.as_view(), name='class-reviews'),
    path('class/<int:pk>/edits', views.ClassDataEdits.as_view(),name='class-edits'),

    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<slug:pk>', views.UserDetail.as_view(), name='user-detail'),
    # 해당 유저가 수강하고 있는 클래스들을 가져오는 것
    path('user/<slug:pk>/class/', views.UserClassList.as_view(), name='user-class'),

    path('notice/', views.NoticeList.as_view(), name='notice-list'),
    path('notice/<int:pk>', views.NoticeDetail.as_view(), name='notice-detail'),

    path('review/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),

    path('edit/', views.EditList.as_view(), name='edit-list'),
    path('edit/<int:pk>',views.EditDetail.as_view(), name='edit-detail'),
    path('edit/<int:pk>/users' ,views.EditUserList.as_view(), name='edit-user-list'),

    path('playstore/', views.play_store_info)
]

urlpatterns += format_suffix_patterns(urlpatterns)
