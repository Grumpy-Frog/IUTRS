from django.forms import ModelForm


from projects.models import Our_Project

class Our_ProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        

    class Meta:
        model = Our_Project
        fields = '__all__'