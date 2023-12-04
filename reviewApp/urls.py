from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.see_all_students, name='see_all_students'),
    path('get-reviews/', views.get_reviews, name='get_reviews'),
    path('get-user-type/', views.get_user_type, name='get_user_type'),
    path('search-users/', views.search_users, name='search_users'),
    path('students/<int:student_id>/', views.see_student, name='see_student'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/add_review/', views.add_review, name='add_review'),
    path('see_reviews_on_me/', views.see_reviews_on_me, name='see_reviews_on_me'),
    path('see_my_reviews/', views.see_my_reviews, name='see_my_reviews'),
    path('see_instructor_reviews/', views.see_instructor_reviews, name='see_instructor_reviews'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]
