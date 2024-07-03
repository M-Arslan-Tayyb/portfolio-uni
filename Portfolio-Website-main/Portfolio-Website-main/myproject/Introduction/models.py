from django.db import models

# Create your models here.


class intro(models.Model):
    name = models.CharField(max_length=50)
    skill = models.TextField()
    subject = models.TextField()
    aboutme = models.TextField()
    teach_stack = models.TextField()
    education = models.TextField()
    experience = models.TextField()


    def __str__(self):
        return self.name

    def get_skills_list(self):
        return self.skill.split(',')

