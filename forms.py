from django.forms import ModelForm
from .models import TeachingRegistration,VolenteerRegistration,Education


class NameForm(ModelForm):
    class Meta:
        model = TeachingRegistration
        fields = "__all__"
class VolenteerForm(ModelForm):
    class Meta:
        model = VolenteerRegistration
        fields = "__all__"
        exclude = ["user"]

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        exclude = ["user"]
