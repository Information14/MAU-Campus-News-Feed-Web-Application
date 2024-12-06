from .models import Campuslogin, Newslogin, Register , Adminnewsmodel, Admincampusmodel, Newscomement, Campuscomement
from django.forms import ModelForm 
from django import forms
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import CKEditor5Widget


class Campusloginform(ModelForm):
    class Meta: 
        model = Campuslogin
        fields = "__all__"



class Newsloginform(ModelForm):
    class Meta: 
        model = Newslogin
        fields = "__all__"
     

    
interesttype = (
    ("News", "News"),
    ("Campus", "Campus"),    
)

class RegisterForm(ModelForm):
    application = forms.MultipleChoiceField(
        choices=interesttype,
        widget=forms.CheckboxSelectMultiple, 
        required=True,  
        error_messages={'required': 'Please select at least one interest.'}
    )
    class Meta: 
        model = Register
        fields = "__all__"


class Adminnewsform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["main"].required = False

    class Meta:
        model = Adminnewsmodel  
        fields = "__all__"


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Title',}),

            'blog': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),

            'person': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),

            'content': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'News Content'}),

            'main': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              ),

            'created_at': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',  
                    'required': 'true',  
                }
            ),                                        
        }

        labels = {
            'title': 'Title', 
            'blog': 'Blog Image',
            'person': 'Admin Image',
            'content': 'News Content',
            'main': 'Main News',
            'author': 'Author',
        }
    

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),  
        widget=forms.Select(attrs={'class': 'form-control'}),  
        required=True
    )



class Admincampusform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["main"].required = False

    class Meta:
        model = Admincampusmodel  
        fields = "__all__"



        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Title',}),

            'blog': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),

            'person': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),

            'content': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'News Content',}),

            'main': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              ),

            'created_at': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',  
                    'required': 'true',  
                }
            ),                                        
        }

        labels = {
            'title': 'Title', 
            'blog': 'Blog Image',
            'person': 'Admin Image',
            'content': 'News Content',
            'main': 'Main News',
            'author': 'Author',
        }
    

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),  
        widget=forms.Select(attrs={'class': 'form-control'}),  
        required=True
    )



    
class Newscommentform(forms.ModelForm):
    class Meta:
        model = Newscomement  
        fields = ['first', 'last', 'message']


    
class Campuscommentform(forms.ModelForm):
    class Meta:
        model = Campuscomement  
        fields = ['first', 'last', 'message']