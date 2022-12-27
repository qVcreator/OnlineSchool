
from django.shortcuts import render

from .models import *


# Create your views here.
def main_window_categories(req):
    cats = Category.objects.all()
    context = {
        'cats': cats
    }
    return render(req, 'course/cats.html', context=context)


def get_courses_by_category_id(req, cat_id):
    courses = Course.objects.filter(cat_id=cat_id)
    context = {
        'courses': courses
    }
    return render(req, 'course/courses.html', context=context)


def get_lessons_by_course_id(req, course_id):
    lessons = Lesson.objects.filter(course_id=course_id)
    context = {
        'lessons': lessons
    }
    return render(req, 'course/course.html', context=context)


def get_lesson(req, lesson_id):
    return render(req, 'course/lesson.html', {'lesson_id': lesson_id})
