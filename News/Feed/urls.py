from .views import NewsView, CampusView, RegisterView, SuccessView, AdminNewsCreateView, IndexView, AdminCampusCreateView, Newsdetail, Campusdetail 
from . import views
from django.urls import path, include

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),

    path('news/', NewsView.as_view(), name='news'),

    path('campus/', CampusView.as_view(), name='campus'),

    path('register/', RegisterView.as_view(), name="register"),

    path('success/', SuccessView.as_view(), name='success'),

    path('news/adminnews', AdminNewsCreateView.as_view(), name='adminnews'),

    path('campus/admincampus', AdminCampusCreateView.as_view(), name='admincampus'),

    path('news/', views.logout_news, name='logoutnews'),

    path('campus/', views.logout_news, name='logoutcampus'),

    path('news/<int:pk>/', Newsdetail.as_view(), name='detailnews'),

    path('campus/<int:pk>/', Campusdetail.as_view(), name='detailcampus'),
]
