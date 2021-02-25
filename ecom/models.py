from django.db import models


# Create your models here.
class LabExam(models.Model):
    exam_date = models.DateField(auto_now_add=True)
    exam_name = models.CharField(max_length=50)
    exam_description = models.TextField(max_length=200)
    total_marks = models.FloatField(max_length=10)
    pass_mark = models.FloatField(max_length=10)
    exam_status = models.BooleanField()

    def __str__(self):
        return self.exam_name

