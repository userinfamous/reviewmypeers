from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=255, default='')
    student_id = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=255)
    work_ethic = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    timeliness = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    leadership_skills = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    charisma = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    agreeable = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    pragmatic = models.BooleanField(blank=True, null=True)  # Default is not needed here as it's nullable
    reliability = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    trustworthiness = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} ({self.university})"

class Review(models.Model):
    reviewer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='given_reviews')
    reviewee = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='received_reviews')
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    class_code = models.CharField(max_length=10, default="",) 
    project_title = models.CharField(max_length=100, default="")
    
    work_ethic = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    timeliness = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    leadership_skills = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    charisma = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    agreeable = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    pragmatic = models.BooleanField(blank=True, null=True) 
    reliability = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    trustworthiness = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review by {self.reviewer} for {self.reviewee}"
    
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    university = models.CharField(max_length=255, default='')
    instructor_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    class_code = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name

class InstructorReview(models.Model):
    student_reviewer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='given_instructor_reviews')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='received_reviews')
    created_at = models.DateTimeField(default=datetime.datetime.now)
    class_code = models.CharField(max_length=10, default='')
    text = models.TextField(max_length=1000, default='')
    
    teaching_ability = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    hard_grader = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    articulate = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    charisma = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    interesting = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    timeliness = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review by {self.student_reviewer} for {self.instructor.name}"



