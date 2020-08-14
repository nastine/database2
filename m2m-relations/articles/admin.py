from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Section

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        # for form in self.forms:
        count = 0 
        for form in self.forms: 
            try:
                if form.cleaned_data['is_main']: 
                    count += 1 
            except KeyError:
                pass
        if count < 1:  
            raise ValidationError('Определите основной тег')
        if count > 1:  
            raise ValidationError('Основной тег может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Section
    formset = RelationshipInlineFormset


@admin.register(Scope)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]