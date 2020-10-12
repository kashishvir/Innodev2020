from django.db import models

# Create your models here.
class Detail(models.Model):
    student_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=15)
    grade = models.IntegerField(default='0')

    def __str__(self):
        return self.username


