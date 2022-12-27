from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_lesson(lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return lesson
