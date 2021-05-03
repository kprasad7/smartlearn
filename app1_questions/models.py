from django.db import models

class Textbook(models.Model):
    clss = [
        ("10" , "10"),
        ("9" , "9"),
        ("8" , "8"),
        ("7" , "7"),
        ("6" , "6"),
        ("ten", "ten")
    ]
    idd = models.PositiveIntegerField(primary_key=True)
    student_class = models.CharField(max_length=10 , choices=clss , default="10")
    subject = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)    
    subtopic = models.CharField(max_length=100 or None)
    

    class Meta:
        abstract = True

class Questions(Textbook):
    image = models.ImageField(upload_to='questions_img', blank=True )
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    
    def __str__(self):
        return self.question
    #def __str__(self):
        #return f'{self.image.url}'
    
    
