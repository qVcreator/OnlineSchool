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
