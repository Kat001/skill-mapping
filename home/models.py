from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    event_text1 = models.TextField(null=True, blank=True)
    event_text2 = models.TextField(null=True, blank=True)
    event_text3 = models.TextField(null=True, blank=True)
    event_text4 = models.TextField(null=True, blank=True)
    event_text5 = models.TextField(null=True, blank=True)
    event_text6 = models.TextField(null=True, blank=True)
    event_text7 = models.TextField(null=True, blank=True)
    event_image = models.ImageField(upload_to='images/event', null=True, blank=True)
    # event_image = models.

    def __str__(self):
        return self.event_name


class Project(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    heading1 = models.CharField(max_length=256, null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    heading2 = models.CharField(max_length=256, null=True, blank=True)
    text21 = models.TextField(null=True, blank=True)
    text22 = models.TextField(null=True, blank=True)
    text23 = models.TextField(null=True, blank=True)
    text24 = models.TextField(null=True, blank=True)
    text25 = models.TextField(null=True, blank=True)
    heading3 = models.CharField(max_length=256, null=True, blank=True)
    text31 = models.TextField(null=True, blank=True)
    text32 = models.TextField(null=True, blank=True)
    text33 = models.TextField(null=True, blank=True)
    text34 = models.TextField(null=True, blank=True)
    text35 = models.TextField(null=True, blank=True)
    heading4 = models.CharField(max_length=256, null=True, blank=True)
    text41 = models.TextField(null=True, blank=True)
    text42 = models.TextField(null=True, blank=True)
    text43 = models.TextField(null=True, blank=True)
    text44 = models.TextField(null=True, blank=True)
    text45 = models.TextField(null=True, blank=True)
    project_image1 = models.ImageField(upload_to='images/project', null=True, blank=True)
    project_image2 = models.ImageField(upload_to='images/project', null=True, blank=True)
    project_image3 = models.ImageField(upload_to='images/project', null=True, blank=True)
    project_image4 = models.ImageField(upload_to='images/project', null=True, blank=True)
    project_image5 = models.ImageField(upload_to='images/project', null=True, blank=True)
    project_image6 = models.ImageField(upload_to='images/project', null=True, blank=True)

    def __str__(self):
        return self.name


