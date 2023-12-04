from django.contrib import admin
from .models import Student, Review, Instructor, InstructorReview

admin.site.register(Student)
admin.site.register(Review)
admin.site.register(Instructor)
admin.site.register(InstructorReview)

