from datetime import date

from haystack.generic_views import SearchView
from django import forms
from haystack.forms import ModelSearchForm, model_choices

from django.utils.translation import gettext_lazy as _
from django.forms.widgets import Input


class MyCheckboxSelectMultiple(forms.RadioSelect):
    allow_multiple_selected = True
    input_type = "checkbox"
    template_name = "search/widgets/checkbox_select.html"
    option_template_name = "search/widgets/checkbox_option.html"

    def use_required_attribute(self, initial):
        return False

    def value_omitted_from_data(self, data, files, name):
        return False


class MyTextInput(Input):
    input_type = "text"
    template_name = "search/widgets/text.html"


class MyModelSearchForm(ModelSearchForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["models"] = forms.MultipleChoiceField(
            choices=model_choices(),
            required=False,
            label=_(""),
            widget=MyCheckboxSelectMultiple,
        )
        self.fields["q"] = forms.CharField(
            required=False,
            label=_(""),
            widget=MyTextInput(attrs={"type": "search"}),
        )


class MySearchView(SearchView):
    """My custom search view."""

    template_name = "search/search-v2.html"
    form_class = MyModelSearchForm
