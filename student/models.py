from django.db import models

class UserProfile(models.Model):
    student_id=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    pincode=models.CharField(max_length=10)
    standard=models.IntegerField()
    phone_number=models.IntegerField()
    
    def __str__(self):
        return self.student_id
