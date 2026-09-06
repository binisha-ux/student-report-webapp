from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AcademicSession(models.Model):
    year = models.IntegerField(max_length=50)     #returns 2026-2027

    def __str__(self):
        return self.year


class SchoolClass(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.class_name} - {self.section}"

class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.sub_name} ({self.sub_code})"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    employee_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    roll_num = models.CharField(max_length=20, unique=True)
    current_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.roll_num})"

class TeacherSubAssignment(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher.user.username} -> {self.subject} [{self.school_class.class_name}]"

class Mark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)
    
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject.code}: {self.marks_obtained}"



