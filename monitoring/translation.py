from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from monitoring.models import Subject, Variant, Topic, Exercise, Result


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Variant)
class VariantTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Topic)
class TopicTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Exercise)
class ExerciseTranslationOptions(TranslationOptions):
    fields = ('text', 'answer_a', 'answer_b', 'answer_c', 'answer_d',)


@register(Result)
class ResultTranslationOptions(TranslationOptions):
    pass
