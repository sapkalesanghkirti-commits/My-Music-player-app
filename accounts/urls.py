from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('signup/', views.signupPage, name='signup'),
    path('profile', views.profile, name='profile'),
    path('support/', views.support_view, name='support'),
    path('premium/', views.premium_view, name='premium'),

    path('follow/', views.follow),
    path('unfollow/', views.unfollow)
]
