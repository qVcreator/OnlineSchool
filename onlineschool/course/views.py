from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


# Create your views here.
def main_window_categories(req):
    cats = Category.objects.all()
    context = {
        'cats': cats
    }
    if req.user.is_authenticated:
        return render(req, 'course/cats.html', context=context)
    else:
        return redirect('login')


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


def home_page(req):
    return render(req, 'course/homepage.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'course/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('categories')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'course/login.html'

    def get_success_url(self):
        return reverse_lazy('categories')


def logout_user(request):
    logout(request)
    return redirect('home')
