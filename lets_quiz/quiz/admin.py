from django.contrib import admin

from .models import Question, Choice,QuizProfile,AttemptedQuestion,Payment
from .forms import QuestionForm, ChoiceForm, ChoiceInlineFormset
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    can_delete = False
    max_num = Choice.MAX_CHOICES_COUNT
    min_num = Choice.MAX_CHOICES_COUNT
    form = ChoiceForm
    formset = ChoiceInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChoiceInline, )
    list_display = ['html', 'is_published']
    list_filter = ['is_published']
    search_fields = ['html', 'choices__html']
    form = QuestionForm

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     if obj is not None and obj.pk is not None and obj.is_published is True:
    #         return False
    #     return True


admin.site.register(Question, QuestionAdmin)
@admin.register(QuizProfile)
class QuizProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','total_score']

@admin.register(AttemptedQuestion)
class AttemptedQuestionModelAdmin(admin.ModelAdmin):
    list_display = ['question','quiz_profile','selected_choice','is_correct','marks_obtained']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['user','payment_done']
