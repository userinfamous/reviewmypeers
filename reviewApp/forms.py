from django import forms
from .models import Student, Review, InstructorReview

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'university',
            'student_id',
            'name',
            'work_ethic',
            'timeliness',
            'leadership_skills',
            'charisma',
            'agreeable',
            'pragmatic',
            'reliability',
            'trustworthiness'
        ]

class InstructorForm(forms.ModelForm):
    class Meta:
        model = InstructorReview
        fields = [
            'student_reviewer',
            'instructor',       # CharField for instructor's name
            'class_code',
            'text',             # TextField for additional comments
            'teaching_ability', # IntegerField for teaching ability rating
            'hard_grader',      # IntegerField for hard grader rating
            'articulate',       # IntegerField for articulation rating
            'charisma',         # IntegerField for charisma rating
            'interesting',      # IntegerField for interesting rating
            'timeliness',       # IntegerField for timeliness rating
        ]
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'reviewer',          # ForeignKey to Student for the reviewer
            'reviewee',          # ForeignKey to Student for the reviewee
            'text',              # Text field for review text
            'class_code',        # CharField for class code
            'project_title',     # CharField for project title
            'work_ethic',        # IntegerField for work ethic rating
            'timeliness',        # IntegerField for timeliness rating
            'leadership_skills', # IntegerField for leadership skills rating
            'charisma',          # IntegerField for charisma rating
            'agreeable',         # IntegerField for agreeableness rating
            'pragmatic',         # BooleanField for pragmatism
            'reliability',       # IntegerField for reliability rating
            'trustworthiness',   # IntegerField for trustworthiness rating
        ]

