from django.db import models
from testing.models import Testing


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255, verbose_name="ФИО преподавателя")

    def __str__(self):
        return self.teacher_name

    class Meta:
        ordering = ('teacher_name',)
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name="группа")

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('group_name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class ResultData(models.Model):
    learner_fio = models.CharField(max_length=255, verbose_name="Данные обучающегося")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", blank=True, null=True)
    who_conducts = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Кто проводил тестирование", blank=True, null=True)
    test_date = models.DateTimeField(verbose_name="Дата прохождения теста", auto_now_add=True)
    score = models.FloatField(verbose_name="Результат теста", blank=True, null=True)
    test = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name="Данные по тесту")
    answers = models.CharField(max_length=255, verbose_name="Ответы", blank=True, null=True)

    def __str__(self):
        return self.learner_fio

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Результат тестирования'
        verbose_name_plural = 'Результаты тестирования'




