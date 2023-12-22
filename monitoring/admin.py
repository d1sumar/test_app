from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from monitoring.models import Subject, Variant, Exercise, Topic, Teacher


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# @admin.register(Answer)
# class AnswerAdmin(admin.TabularInline):
#     model = Answer
#     extra = 4


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ['subject']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ['variant']
