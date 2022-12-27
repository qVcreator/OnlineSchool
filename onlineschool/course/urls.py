from django.urls import path

from .views import *

urlpatterns = [
    path('', main_window_categories, name="home"),
    path('categories/<int:cat_id>', get_courses_by_category_id, name="courses_by_category")
]
