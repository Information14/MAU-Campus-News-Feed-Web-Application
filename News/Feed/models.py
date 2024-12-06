from django.db import models
from django.contrib.auth.models import User  
from django_ckeditor_5.fields import CKEditor5Field


class Campuslogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Campuslogin'
        verbose_name_plural = 'Campuslogin List'

    def __str__(self) -> str:
        return f'{self.username}'


class Newslogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Newslogin'
        verbose_name_plural = 'Newslogin List'

    def __str__(self) -> str:
        return f'{self.username}'


leveltype = (
    ("100", "100"),
    ("200", "200"), 
    ("300", "300"),
    ("400", "400"),
    ("500", "500"),   
)

class Register(models.Model):
    first = models.CharField(max_length=150)
    last = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    application = models.TextField(default="Choose your interest")
    level = models.CharField(max_length=50, choices=leveltype, default="Choose your level")

    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Register List'

    def __str__(self) -> str:
        return f'{self.first}' + " " + f'{self.last}' 
    

class Adminnewsmodel(models.Model): 
    title = models.CharField(max_length=128)
    blog = models.ImageField(upload_to='img/blog/')
    person = models.ImageField(upload_to='img/person/')
    content = models.CharField(max_length=128)
    main = CKEditor5Field(null=True, blank=True, config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Adminnewsmodel'
        verbose_name_plural = 'Adminnewsmodel List'

    def __str__(self) -> str:
        return f'{self.title}'




class Newscomement(models.Model): 
    post = models.ForeignKey(Adminnewsmodel,on_delete=models.CASCADE,related_name='comments')
    first = models.CharField(max_length=150)
    last = models.CharField(max_length=150)
    message = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Newscomement'
        verbose_name_plural = 'Newscomement List'

    def __str__(self) -> str:
        return f'{self.first}' + " " + f'{self.last}'




class Admincampusmodel(models.Model): 
    title = models.CharField(max_length=128)
    blog = models.ImageField(upload_to='img/blog/')
    person = models.ImageField(upload_to='img/person/')
    content = models.CharField(max_length=128)
    main = CKEditor5Field(null=True, blank=True,config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Admincampusmodel'
        verbose_name_plural = 'Admincampusmodel List'

    def __str__(self) -> str:
        return f'{self.title}' 



class Campuscomement(models.Model): 
    post = models.ForeignKey(Admincampusmodel,on_delete=models.CASCADE,related_name='comments')
    first = models.CharField(max_length=150)
    last = models.CharField(max_length=150)
    message = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Campuscomement'
        verbose_name_plural = 'Campuscomement List'

    def __str__(self) -> str:
        return f'{self.first}' + " " + f'{self.last}'    




    
