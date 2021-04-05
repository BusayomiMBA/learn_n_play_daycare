from django import forms
from .models import Daily_Activity, Child

class Daily_ActivityForm(forms.ModelForm):
    # meta class beacuse that's how django can do it
    class Meta:
        # which model
        model = Daily_Activity
        fields = ['date', 'time', 'activity']

# added a catform
class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child_image', 'name', 'age', 'gender', 'address', 'pcp', 'bio']