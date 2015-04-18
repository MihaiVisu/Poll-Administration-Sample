from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Text',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #display the list names
    list_display = ('question_text', 'pub_date','was_published_recently')
    #add a list of filters to the Questions page in the admin section
    list_filter = ['pub_date']
    #add a search field to the Questions page in the admin section
    search_fields = ['questions_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)