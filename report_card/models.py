from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(blank=False)
    student_age = models.IntegerField(default=18)
    student_email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.student_name}"


class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.sub_name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f'{self.student.student_name} - {self.subject.sub_name} - {self.marks_obtained}'