from django.contrib import admin

from . import models


class TextInline(admin.StackedInline):
    model = models.Text


class QuizInline(admin.StackedInline):
    model = models.Quiz


class AnswerInline(admin.StackedInline):
    model = models.Answer

    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]
    
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    
    
class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']
    
    
class TextAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'order', 'description']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
