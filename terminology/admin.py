from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django.contrib import admin
from .models import Term


class TermAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parents'].queryset = Term.objects.exclude(pk=self.instance.pk)
        self.fields['parents'].required = False

    class Meta:
        widgets = {
            'parents': FilteredSelectMultiple(verbose_name='Related terms', is_stacked=False),
        }


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'explanation')
    form = TermAdminForm
