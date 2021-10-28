from django.forms import ModelForm
from .models import Form


class CVForm(ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
        labels = {
            "language1": "First language",
            "language2": "Second language (optional)",
            "language3": "Third language (optional)",
            "skill1": "First skill",
            "skill2": "Second skill",
            "skill3": "Third skill (optional)",
            "skill4": "Fourth skill (optional)",
            "skill5": "Fifth skill (optional)",
            "skill6": "Sixth skill (optional)"
        }

    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key != "picture" and key != "about":
                field.widget.attrs.update({'class': 'inputclass'})
            elif key == "about":
                field.widget.attrs.update({'class': 'aboutclass'})


