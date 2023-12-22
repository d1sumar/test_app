from django.shortcuts import render, redirect
from django.views import View

from monitoring.forms.forms import VariantForm, ExerciseFormSet
from monitoring.models import Subject, Variant, Exercise, Result, UserAnswer


# Create your views here.
def index_view(request):
    return render(request, 'pages/home_page.html')


def subject_list_view(request):
    user = request.user
    subject_list = Subject.objects.all()
    if request.user.is_staff:
        subject_list = Subject.objects.all()
        if user.is_staff:
            subject_list = subject_list.filter(teacher__user=user)
    context = {
        "subject_list": subject_list
    }
    return render(request, 'pages/subjects_page.html', context)


def subjects_view(request, pk):
    variant_list = Variant.objects.filter(subject_id=pk)
    context = {
        'variant_list': variant_list
    }
    return render(request, 'pages/variant_page.html', context)


def variants_view(request, pk):
    exercise_list = Exercise.objects.filter(variant_id=pk)
    variant = Variant.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "variant": variant,
            "exercise_list": exercise_list,
        }
        return render(request, 'pages/exercise_page.html', context)

    if request.method == "POST":
        data = request.POST
        result = Result.objects.create(user=request.user, variant=variant)
        for exercise in exercise_list:
            user_answer = UserAnswer(result=result, exercise=exercise)
            if data.get(str(exercise.id)) is not None:
                user_answer.user_answer = data.get(str(exercise.id))
                if exercise.answer == data.get(str(exercise.id)):
                    user_answer.is_True = True
                user_answer.save()
            return redirect('monitoring:result', pk=result.id)


class VariantCreateView(View):
    def get(self, request):
        if request.user.is_staff == 1:
            context = {
                'variant_form': VariantForm(),
                'formset': ExerciseFormSet(instance=Variant())
            }
            return render(request, 'pages/variant_create.html', context=context)
        else:
            return redirect('404.html')

    def post(self, request):
        variant_form = VariantForm(request.POST)
        formset = ExerciseFormSet(request.POST, instance=Variant())

        if variant_form.is_valid() and formset.is_valid():
            variant = variant_form.save()
            formset.instance = variant
            formset.save()
            return render('home')


def result_list_view(request):
    context = {
        'result_list': request.user.results.all().order_by('-date_completed')
    }
    return render(request, 'pages/result_list_page.html', context)


def result_view(request, pk):
    result = Result.objects.get(id=pk)
    ua = UserAnswer.objects.filter(result=result, is_True=True)

    object_list = []
    for execise in result.variant.exercises.all():
        object_list.append({
            'exercise': execise,
            'user_answer': execise.user_answers.get(result=result).user_answer,
            'is_True': execise.user_answers.get(result=result).is_True
        })

    context = {
        'object_list': object_list,
        'ball': len(ua),
        'count': len(result.variant.exercises.all()),
    }
    return render(request, 'pages/result_page.html', context)
