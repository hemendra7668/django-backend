from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class AddUser(AbstractUser):
    email= models.EmailField(blank=False, verbose_name="user mail id", max_length=50)
    USERNAME_FIELD='username'
    EMAIL_FIELD='email'
    
class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name;     
    
    
class Quizes(models.Model):
    title=models.CharField(max_length=250,default="new quizz")
    Category= models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING)
    date_created=models.DateTimeField()
    
    def __str__(self):
        return self.title;     
    

class Questions(models.Model):
    SCALE= (
       ('0', 'fundamental'),   
       ('1', 'beginner'),   
       ('2', 'intermediate'),   
       ('3', 'advance'),   
       ('4', 'expert'),   
    )
    TYPE= (
        (0,('multiple choices')),  
    )
    
    quiz = models.ForeignKey(Quizes, related_name='questions', on_delete=models.DO_NOTHING)
    technique= models.IntegerField(choices= TYPE, default=0,verbose_name="type of questions")
    title= models.CharField(max_length=120, verbose_name="title")
    difficulty= models.IntegerField(choices=SCALE, default=0,verbose_name="difficulty")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    is_active = models.BooleanField( default=False, verbose_name="active status")
    
    def __str__(self):
        return self.title;     
    
    
class Answer(models.Model):
    question = models.ForeignKey( Questions, related_name='answers', on_delete=models.DO_NOTHING)
    answer_text= models.CharField(max_length=50, verbose_name="answert text")
    is_right= models.BooleanField(default=False) 
    
    def __str__(self):
        return self.answer_text
    

    