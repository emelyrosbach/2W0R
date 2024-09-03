from django import forms
from vue.models import Experiment
from django.core.exceptions import ObjectDoesNotExist
from django.core import validators

class RegistrationBaseline(forms.Form):
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(
    attrs={'type': 'email',
           'placeholder': ('example@app.com')}))
    terms = forms.BooleanField(required=True) 

def validate_email(email):
    try:
        Experiment.objects.get(email=email)
    except ObjectDoesNotExist:
        raise forms.ValidationError("E-mail not used in round 1!")

class RegistrationXAI(forms.Form):   
    email = forms.EmailField(label="", required=True,validators=[validate_email], widget=forms.TextInput(
    attrs={'type': 'email',
           'placeholder': ('example@app.com')}))
    terms = forms.BooleanField(required=True)

class PreStudy(forms.Form):
    GENDEROPTS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
        ('Other', 'Other'),
    ]
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDEROPTS,
        label="What gender do you identify as?",
        required=True
    )
    AGEOPTS = [
        ('<18', '<18'),
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('>55', '>55'),
    ]
    age = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=AGEOPTS,
        label="What is your age?",
        required=True
    )
    EXPOPTS = [
        ('<5 years', '<5 years'),
        ('5-10 years', '5-10 years'),
        ('10-15 years', '10-15 years'),
        ('>15 years', '>15years'),
    ]
    experience = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=EXPOPTS,
        label="What is the duration of your experience working in the medical field?",
        required=True
    )
    INTERESTOPTS = [
        ('5', 'Very interested in technology'),
        ('4', 'Somehow interested in technology'),
        ('3', 'Indifferent about technology'),
        ('2', 'Less interested in technology'),
        ('1', 'Not at all interested in technology'),
    ]
    interest = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=INTERESTOPTS,
        label="How interested in technology would you describe yourself?",
        required=True
    )
    ADOPTOPTS = [
        ('4', 'I will try out the app as soon as possible.'),
        ('3', 'I will start using the app as soon as it becomes popular among my acquaintances.'),
        ('2', 'I will eventually give in to using the app, despite initially resisting it.'),
        ('1', 'I will strongly oppose the use of the app'),
    ]
    adopt = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=ADOPTOPTS,
        label="A new messenger app is coming onto the market. Which statement applies to you?",
        required=True
    )
    AIEXPOPTS = [
        ('4', 'Very much familiar'),
        ('3', 'Somewhat familiar'),
        ('2', 'Less familiar'),
        ('1', 'Not at all familiar'),
    ]
    aiexp = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=AIEXPOPTS,
        label="How familiar are you with artificial intelligence?",
        required=True
    )

class PostStudy(forms.Form):
    CHOICES = [
        ('1', ''),
        ('2', ''),
        ('3', ''),
        ('4', ''),
        ('5', ''),
        ('6', ''),
        ('7', ''),
    ]
    item1 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item2 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item3 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item4 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item5 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item6 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item7 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
    item8 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )

class PostStudyXAI(forms.Form):
    CHOICES = [
        ('1', ''),
        ('2', ''),
        ('3', ''),
        ('4', ''),
        ('5', ''),
        ('6', ''),
        ('7', ''),
        ('8', ''),
        ('9', ''),
        ('10', '')
    ]
    question1 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="1. How satisfied are you with the overall performance of the AI tool?",
        required=True
    )
    question2 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="2. How helpful do you find the AI tool in assisting your tasks?",
        required=True
    )
    question3 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="3. Do you trust the recommendations provided by the AI tool?",
        required=True
    )
    question4 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="4. Do you believe the AI tool provides accurate results?",
        required=True
    )
    question5 = forms.CharField(label="5. Have you encountered any errors or limitations while using the AI tool? If yes, please describe.", required=True)
    question6 = forms.CharField(label="6. Do you have any suggestions for improving the functionality or usability of the AI tool?", required=True)


class Confidence(forms.Form):
    CHOICES = [
        ('1', ''),
        ('2', ''),
        ('3', ''),
        ('4', ''),
        ('5', ''),
    ]
    likertScale = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label="",
        required=True
    )
