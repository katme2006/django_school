from django.db import models
from .validators import validate_name, validate_student_email, validate_locker_combination
from django.core import validators as v
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, validators=[validate_name])
    student_email = models.EmailField(unique=True, blank=False, null=False, validators=[validate_student_email])
    personal_email = models.EmailField(unique=True)
    locker_number = models.IntegerField(unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default ="12-12-12", validators=[validate_locker_combination])
    good_student = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, num):
        self.locker_number = num

    def student_status(self,bool):
        self.good_student = bool


