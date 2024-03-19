from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import ProfileForm, SkillForm, ExperienceForm, LanguageForm, AdditionalSkillForm
from .models import Profile, Skill, Experience, Language, AdditionalSkill

def create_profile(request):
    SkillFormSet = inlineformset_factory(Profile, Skill, form=SkillForm, extra=1, can_delete=True)
    ExperienceFormSet = inlineformset_factory(Profile, Experience, form=ExperienceForm, extra=1, can_delete=True)
    LanguageFormSet = inlineformset_factory(Profile, Language, form=LanguageForm, extra=1, can_delete=True)
    AdditionalSkillFormSet = inlineformset_factory(Profile, AdditionalSkill, form=AdditionalSkillForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            created_profile = profile_form.save(commit=False)
            skill_formset = SkillFormSet(request.POST, instance=created_profile)
            experience_formset = ExperienceFormSet(request.POST, instance=created_profile)
            language_formset = LanguageFormSet(request.POST, instance=created_profile)
            additional_skill_formset = AdditionalSkillFormSet(request.POST, instance=created_profile)
            
            if skill_formset.is_valid() and experience_formset.is_valid() and language_formset.is_valid() and additional_skill_formset.is_valid():
                created_profile.save()
                skill_formset.save()
                experience_formset.save()
                language_formset.save()
                additional_skill_formset.save()
                return redirect('display_profile', profile_id=created_profile.id)
    else:
        profile_form = ProfileForm()
        skill_formset = SkillFormSet()
        experience_formset = ExperienceFormSet()
        language_formset = LanguageFormSet()
        additional_skill_formset = AdditionalSkillFormSet()

    context = {
        'profile_form': profile_form,
        'skill_formset': skill_formset,
        'experience_formset': experience_formset,
        'language_formset': language_formset,
        'additional_skill_formset': additional_skill_formset,
    }
    return render(request, 'create_profile.html', context)
def display_profile(request, profile_id):
    # Lấy thông tin Profile dựa vào profile_id
    profile = Profile.objects.get(id=profile_id)
    
    # Lấy tất cả thông tin Skills, Experience, Language, và Additional Skills liên quan đến Profile này
    skills = Skill.objects.filter(profile=profile)
    experiences = Experience.objects.filter(profile=profile)
    languages = Language.objects.filter(profile=profile)
    additional_skills = AdditionalSkill.objects.filter(profile=profile)

    # Truyền tất cả thông tin này vào context để sử dụng trong template
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'languages': languages,
        'additional_skills': additional_skills,
    }

    return render(request, 'cv1.html', context)
