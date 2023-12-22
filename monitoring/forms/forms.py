from django.forms import ModelForm, inlineformset_factory

from monitoring.models import Variant, Exercise


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = ['title', 'title_uz', 'title_ru', 'title_en']


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'


ExerciseFormSet = inlineformset_factory(
    Variant,
    Exercise,
    fields=[
        'topic',
        'text', 'text_uz', 'text_ru', 'text_en',
        'answer_a', 'answer_a_uz', 'answer_a_ru', 'answer_a_en',
        'answer_b', 'answer_b_uz', 'answer_b_ru', 'answer_b_en',
        'answer_c', 'answer_c_uz', 'answer_c_ru', 'answer_c_en',
        'answer_d', 'answer_d_uz', 'answer_d_ru', 'answer_d_en',
        'answer'
    ],
    extra=3,
    can_delete=False
)
