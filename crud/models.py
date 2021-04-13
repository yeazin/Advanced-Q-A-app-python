from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quser(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='users')
    email = models.EmailField(blank=True)
    username = models.CharField(blank=False, max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return f"{self.username} | {self.user}"

class Topics(models.Model):
    name    = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name 
class Question(models.Model):
    user = models.ForeignKey(Quser, on_delete=models.DO_NOTHING, null=True, related_name='q_user')
    q_name = models.CharField(max_length=300, blank=False, null=True, verbose_name='Question')
    topics = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.q_name

    class Meta:
        verbose_name = " Questions"
        verbose_name_plural = 'Questions'

# made by  Yeasin
# facebook : fb.com/yeariha.farsin
# github : github.com/yeazin
# contact : naz.yeasin@gmail.com