
from django import forms
from django_bpmn.widget import BPMNWidget

from sample.models import BPMN


class BPMNForm(forms.Form):
    diagram = forms.CharField(widget=BPMNWidget)


class BPMNModelForm(forms.ModelForm):
    diagram = forms.CharField(widget=BPMNWidget)

    class Meta:
        model = BPMN
        exclude = ()
