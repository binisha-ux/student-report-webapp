from django.contrib import admin
from .models import (
    AcademicSession,
    SchoolClass,
    Subject,
    TeacherProfile,
    StudentProfile,
    TeacherSubAssignment,
    Mark,
)


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('year',)  

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):  
    list_display = ('class_name', 'section')
    search_fields = ('class_name', 'section')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):  
    list_display = ('sub_name', 'sub_code') 
    search_fields = ('sub_name', 'sub_code')  


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):  
    list_display = ('user', 'employee_id')
    search_fields = ('user__username', 'employee_id')


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):  
    list_display = ('user', 'roll_num', 'current_class')
    list_filter = ('current_class',)
    search_fields = ('user__username', 'roll_num')  


@admin.register(TeacherSubAssignment)
class TeacherSubAssignmentAdmin(admin.ModelAdmin): 
    list_display = ('teacher', 'subject', 'school_class', 'session')
    list_filter = ('session', 'school_class', 'subject')
    search_fields = ('teacher__user__username', 'subject__sub_name', 'school_class__class_name') 

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks_obtained', 'session', 'is_submitted')
    list_filter = ('session', 'is_submitted', 'subject')
    search_fields = ('student__roll_num', 'subject__sub_name')