from django.forms import ModelForm
from .models import Profile, Skill, Experience,Language, AdditionalSkill

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'address', 'profile_image']

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'skill_level']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'date_range']
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'level']

class AdditionalSkillForm(ModelForm):
    class Meta:
        model = AdditionalSkill
        fields = ['skill_name', 'description']