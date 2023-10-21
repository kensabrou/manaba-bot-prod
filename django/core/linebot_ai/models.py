from django.db import models

class LineUserModel(models.Model):
    user_id = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.user_id}"

class Student(LineUserModel):
    manaba_id = models.CharField(max_length=30, blank=True, null=True)
    manaba_password = models.CharField(max_length=30, blank=True, null=True)
