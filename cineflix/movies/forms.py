from django import forms

from .models import Movie

import os 

class MovieForm(forms.ModelForm):

    class Meta :

        model = Movie

        # fields = ['name',]

        # fields = '__all__'

        exclude = ['uuid','active_status']

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Movie name'}),
            
            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'description' : forms.Textarea(attrs={'class':'form-control','rows':3 , 'placeholder':'Enter Movie description'}),

            'release_year' : forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'industry' : forms.Select(attrs={'class':'form-select'}),

            'runtime' : forms.TimeInput(attrs={'class':'form-control','type':'time'},format='%H:%M'),

            'certification' : forms.Select(attrs={'class':'form-select'}),

            'genre' : forms.SelectMultiple(attrs={'class':'form-select'}),

            'artists' : forms.SelectMultiple(attrs={'class':'form-select'}),

            'video' : forms.TextInput(attrs={'class':'form-control','type':'url','placeholder':'Enter video URL'}),

            'tags' : forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter tags with #'}),

            'languages' : forms.SelectMultiple(attrs={'class':'form-select'}),

        }

    def clean(self):

        cleaned_data = super().clean()

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3*1024*1024:

            self.add_error('photo','maximum file size upto 3MB')






        # extension = os.path.splitext(photo.name)[1].lower()

        # if extension not in ['.jpg','.jpeg','.png']:

        #     self.add_error('photo','upload files with extension jpg or jpeg or png  ')

        

    # runtime= forms.TimeInput(input_format=['%H:%M'],widget=forms.TimeInput(attrs={'class':'form-control','type':'time'},format='%H:%M'))
