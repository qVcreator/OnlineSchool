from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('categories/', main_window_categories, name="categories"),
    path('categories/<int:cat_id>', get_courses_by_category_id, name="courses_by_category"),
    path('course/<int:course_id>', get_lessons_by_course_id, name="lessons_by_course"),
    path('lesson/<int:lesson_id>', get_lesson, name='lesson')
]
