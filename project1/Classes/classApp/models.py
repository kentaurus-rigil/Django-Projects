from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(default="", blank=False, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=False, null=False)
    duration = models.FloatField(max_length=60, default="", blank=False, null=False)
