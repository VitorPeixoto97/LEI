from django.contrib import admin

# Register your models here.
from .models import Question, Tecnico, Jogo, Atleta, Formacao, Clube, Gestor
from django.forms import ModelForm
from django.forms.widgets import TextInput



#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 1

#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('',               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
#    inlines = [ChoiceInline]

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

admin.site.register(Jogo)

admin.site.register(Tecnico)

admin.site.register(Gestor)

