from django.db import models

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profiles/')

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_level = models.IntegerField()  # e.g., 75 for 75%

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default="Not specified")

    date_range = models.CharField(max_length=100, default='N/A')

class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default='Beginner')  # Assuming 'Beginner' as a sensible default


class AdditionalSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    description = models.TextField(default="Not specified")

