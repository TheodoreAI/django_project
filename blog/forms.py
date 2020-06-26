from django import forms


# finish the dynamic update of the images
class AboutUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['image']
