from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Review, Instructor, InstructorReview
from .forms import StudentForm, ReviewForm, InstructorForm
from django.db.models import Avg, Q, Count

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a redirect to the login page after registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

@login_required
def see_all_students(request):
    students = Student.objects.all().select_related('user')  # This will prefetch the related User objects
    for student in students:
        # Calculate averages for each category, excluding zero ratings
        student.avg_work_ethic = round(Review.objects.filter(reviewee=student, work_ethic__gt=0).aggregate(Avg('work_ethic'))['work_ethic__avg'] or 0, 1)
        student.avg_timeliness = round(Review.objects.filter(reviewee=student, timeliness__gt=0).aggregate(Avg('timeliness'))['timeliness__avg'] or 0, 1)
        student.avg_leadership_skills = round(Review.objects.filter(reviewee=student, leadership_skills__gt=0).aggregate(Avg('leadership_skills'))['leadership_skills__avg'] or 0, 1)
        student.avg_charisma = round(Review.objects.filter(reviewee=student, charisma__gt=0).aggregate(Avg('charisma'))['charisma__avg'] or 0, 1)
        student.avg_agreeable = round(Review.objects.filter(reviewee=student, agreeable__gt=0).aggregate(Avg('agreeable'))['agreeable__avg'] or 0, 1)
        student.avg_reliability = round(Review.objects.filter(reviewee=student, reliability__gt=0).aggregate(Avg('reliability'))['reliability__avg'] or 0, 1)
        student.avg_trustworthiness = round(Review.objects.filter(reviewee=student, trustworthiness__gt=0).aggregate(Avg('trustworthiness'))['trustworthiness__avg'] or 0, 1)

        # Calculate percentage for pragmatic (assuming it's a BooleanField)
        total_reviews = Review.objects.filter(reviewee=student).count()
        pragmatic_yes = Review.objects.filter(reviewee=student, pragmatic=True).count()
        student.pragmatic_percentage = round((pragmatic_yes / total_reviews * 100) if total_reviews > 0 else 0 or 0, 1)

    return render(request, 'students/see_all_students.html', {'students': students})

@login_required
def get_reviews(request):
    student_id = request.GET.get('student_id')
    reviews = Review.objects.filter(reviewee_id=student_id).values(
        'reviewer__student_id',      # ID of the reviewer
        'reviewer__name',    # Adjust field name as per your Student model
        'reviewee__student_id',      # ID of the reviewee
        'reviewee__name',    # Adjust field name as per your Student model
        'text',
        'created_at',
        'class_code',
        'project_title',
        'work_ethic',
        'timeliness',
        'leadership_skills',
        'charisma',
        'agreeable',
        'pragmatic',
        'reliability',
        'trustworthiness',
    )
    reviews_data = list(reviews)
    return JsonResponse(reviews_data, safe=False)

@login_required
def see_student(request, student_id):
    # This line retrieves the Student object from the database or returns a 404 error if not found
    student = get_object_or_404(Student, student_id=student_id)  
    # This line renders the 'student_detail.html' template, passing the student object as context
    return render(request, 'students/see_student.html', {'student': student})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the list of students
    else:
        form = StudentForm()  # An unbound form
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def add_review(request):
    reviewer = get_object_or_404(Student, user=request.user)
    form = ReviewForm(request.POST or None, initial={'reviewer': reviewer})
    instructor_form = InstructorForm(request.POST or None)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'student' and form.is_valid():
            review = form.save(commit=False)
            review.reviewer = reviewer
            if form.cleaned_data.get('reviewee') == reviewer:
                messages.error(request, "You cannot review yourself.")
            else:
                review.save()
                messages.success(request, "Student review added successfully.")
                return redirect('see_my_reviews')  # Replace with your success URL

        elif form_type == 'instructor' and instructor_form.is_valid():
            instructor_review = instructor_form.save(commit=False)
            instructor_review.student_reviewer = reviewer
            instructor_review.save()
            messages.success(request, "Instructor review added successfully.")
            return redirect('see_my_reviews')

        else:
            messages.error(request, "There was an error with your submission.")

    return render(request, 'students/add_review.html', {
        'form': form, 
        'instructor_form': instructor_form, 
        'reviewer': reviewer
    })


@login_required
def see_reviews_on_me(request):
    # Ensure the logged-in User is associated with a Student object
    username = request.user.username
    name_parts = username.split('.')
    fullname = ' '.join(part.capitalize() for part in name_parts)
    student = get_object_or_404(Student, name=fullname)
    reviews_on_me = Review.objects.filter(reviewee=student)
    return render(request, 'students/see_reviews_on_me.html', {'reviews': reviews_on_me})

@login_required
def see_my_reviews(request):
    is_student = Student.objects.filter(user=request.user).exists()
    reviews, student, instructor_reviews = None, None, None

    if is_student:
        student = get_object_or_404(Student, user=request.user)
        reviews = Review.objects.filter(reviewer=student)
        instructor_reviews = InstructorReview.objects.filter(student_reviewer=student)

    context = {
        'reviews': reviews,
        'instructor_reviews': instructor_reviews,
        'is_student': is_student
    }
    
    return render(request, 'students/see_my_reviews.html', context)


@login_required
def see_instructor_reviews(request):
    # Filter reviews where the 'instructor_review' boolean field is True
    instructor_reviews = InstructorReview.objects.all()
    for review in instructor_reviews:
        review.avg_teaching_ability = round(InstructorReview.objects.filter(id=review.id, teaching_ability__gt=0).aggregate(Avg('teaching_ability'))['teaching_ability__avg'] or 0, 1)
        review.avg_hard_grader = round(InstructorReview.objects.filter(id=review.id, hard_grader__gt=0).aggregate(Avg('hard_grader'))['hard_grader__avg'] or 0, 1)
        review.avg_articulate = round(InstructorReview.objects.filter(id=review.id, articulate__gt=0).aggregate(Avg('articulate'))['articulate__avg'] or 0, 1)
        review.avg_charisma = round(InstructorReview.objects.filter(id=review.id, charisma__gt=0).aggregate(Avg('charisma'))['charisma__avg'] or 0, 1)
        review.avg_interesting = round(InstructorReview.objects.filter(id=review.id, interesting__gt=0).aggregate(Avg('interesting'))['interesting__avg'] or 0, 1)
        review.avg_timeliness = round(InstructorReview.objects.filter(id=review.id, timeliness__gt=0).aggregate(Avg('timeliness'))['timeliness__avg'] or 0, 1)

    return render(request, 'students/see_instructor_reviews.html', {'reviews': instructor_reviews})

@login_required
def search_users(request):
    term = request.GET.get('term')  # jQuery UI sends the term as 'term'
    students = Student.objects.filter(name__icontains=term)[:10]  # Limit results for performance
    student_list = [{'student_id': student.student_id, 'label': student.name, 'value': student.name} for student in students]
    return JsonResponse(student_list, safe=False)

@login_required
def get_user_type(request):
    user_id = request.GET.get('user_id')
    user_type = None

    # Check if a Student with the given user_id exists
    if Instructor.objects.filter(instructor_id=user_id).exists():
        user_type = 'instructor'
    # Check if an Instructor with the given user_id exists
    elif Student.objects.filter(student_id=user_id).exists():
        user_type = 'student'

    return JsonResponse({'user_type': user_type})