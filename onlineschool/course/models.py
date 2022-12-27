from django.db import models
from django.urls import reverse


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="Описание урока")
    video = models.CharField(max_length=255, verbose_name="Ссылка на обучающее видео")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="Источник (курс)")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson', kwargs={'lesson_id': self.pk})

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('courses_by_category', kwargs={'cat_id': self.pk})


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Описание курса")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def get_absolute_url(self):
        return reverse('lessons_by_course', kwargs={'course_id': self.pk})
