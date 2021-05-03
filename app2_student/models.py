from django.db import models
from django.contrib.auth.models import User

class Studentt(models.Model):
    clss = [
        ("10" , "10"),
        ("9" , "9"),
        ("8" , "8"),
        ("7" , "7"),
        ("6" , "6"),
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    classs = models.CharField(max_length=10 , choices=clss , default="10")
    gender=models.CharField(max_length=7)
    mobile = models.CharField(max_length=15,null=False)
    email=models.CharField(max_length=50)
    
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_profile(self):
        return self.profile_pic    
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name