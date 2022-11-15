from django.db import models
from django.contrib.auth.models import User
# Create your models here.
sex = [('Male','Male'),('Female','Female')]

prog_type =[('Part-Time','Part-Time'),('Full-Time','Full-Time')]

class TeacherExtra_1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    teacher_sex = models.CharField(max_length = 200,choices= sex)
    teacher_type = models.CharField(max_length =10,choices = prog_type)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=11)
    teacher_picture = models.ImageField(upload_to="images/teachers/",null = False,blank=False)
    address = models.CharField(max_length=200)
    subject = models.CharField(max_length = 500,null = False,blank=False)
    qualifications = models.TextField(blank =True,null =True)
    teacher_email = models.EmailField(blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('Waec Class','Waec Class'),('Jamb Class','Jamb Class'),('Putme Class','Putme Class'),

    ('School of Nursing Class','School of Nursing Class'),
    ('Art Class','Art Class'),('Commercial Class','Commercial Class'),
    ('Private Class','Private Class')]



university = [('UNN','UNN'),
                ('UNIZIK','UNIZIK'),
                ('FUTO','FUTO'),('UNICAL','UNICAL'),
                ('EBSU','EBSU'),('FUNAI','FUNAI'),
                ('UNTH SON','UNTH SON'),
                ('BISHOP SHANAHAN','BISHOP SHANAHAN'),
                ('NAUTH SON','NAUTH SON'),
                ('FETHA SON','FETHA SON'),
                ('IYIENU','IYIENU'),
                ('PARKLANE','PARKLANE'),
                ('Other SON','Other SON'),
                ('Other Universities')]

hear = [('Social Media','Social Media'),('Friend','Friend'),('Parents or Gaurdian','Parents or Gaurdian')]
class StudentExtra_1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    student_sex = models.CharField(max_length = 200,choices= sex)
    cl= models.CharField(max_length=200,choices=classes,default='Waec Class')
    choice_of_course = models.CharField(max_length=200)
    personal_mobile = models.CharField(max_length=11,null=True)
    fee_paid=models.PositiveIntegerField(null=True)
    profile_picture = models.ImageField(upload_to="images/",null = False,blank=False)
    parent_or_gaurdian_mobile=models.CharField(max_length=11,null=True)
    Parent_gaurdian_name = models.CharField(max_length = 200)
    permanent_address = models.CharField(max_length=200)
    email_address =models.EmailField(max_length=200)
    date_of_birth= models.DateTimeField(blank=True)
    join_date =models.DateTimeField(auto_now_add = True)
    choices_unversity_son = models.CharField(max_length=40)
    hear_about_us = models.CharField(max_length=200,choices = hear,default = 'Social Media')
    status=models.BooleanField(default=False)
    roll = models.CharField(max_length=10,null=True,blank=True)
    special_needs =models.TextField(max_length = 300,null =True,blank = True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)
