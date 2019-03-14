from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import Atleta
from .models import Formacao
from .models import Clube
from django.forms import ModelForm
from django.forms.widgets import TextInput



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

class CategoryForm(ModelForm):
    class Meta:
        model = Clube
        fields = '__all__'
        widgets = {
            'cor': TextInput(attrs={'type': 'color'}),
        }

class ClubeAdmin(admin.ModelAdmin):
    form_class = CategoryForm
    fieldsets = (
        (None, {'fields': ('nome', 'cor')
            }),
        )
    
class FormacaoAdmin(admin.ModelAdmin):
	fieldsets = (
        (None, {'fields': ('nome', 'clube')
            }),
        )



#admin.site.register(Question, QuestionAdmin)

admin.site.register(Atleta)

admin.site.register(Formacao, FormacaoAdmin)

admin.site.register(Clube, ClubeAdmin)

