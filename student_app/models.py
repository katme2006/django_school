from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    student_email = models.EmailField(unique=True, blank=False, null=False)
    personal_email = models.EmailField(unique=True)
    locker_number = models.IntegerField(unique=True, default=110)
    locker_combination = models.CharField(max_length=8, default ="12-12-12")
    good_student = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, num):
        self.locker_number = num

    def student_status(self,bool):
        self.good_student = bool

