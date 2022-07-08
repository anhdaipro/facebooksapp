from django.db import models
from post.models import *
from django.contrib.auth.models import User 
from notifications.models import *
from django.db.models.signals import post_save, post_delete

# Create your models here.
emotion_choice=(
    ('1','like'),
    ('2','love'),
    ('3','wow'),
    ('4','sad'),
    ('5','smile'),
    ('6','indignant'),
)

class Comment(models.Model):
	post = models.ForeignKey(to="post.Post",null=True, on_delete=models.CASCADE, related_name='comments')
	filepost = models.ForeignKey(to="post.Fileuploadpost",null=True, on_delete=models.CASCADE, related_name='file_comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	uploadfile=models.ForeignKey(to="post.Fileupload", on_delete=models.CASCADE,null=True)
	text_preview=models.TextField(null=True)
	tags = models.ManyToManyField(User, related_name='tags_comment',blank=True)
	date = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
	def count_reply(self):	
		return Comment.objects.filter(parent=self).count()
	def count_express_emotions(self):
    		return Comment_emotions.objects.filter(comment=self).count()
	
	
class Reportcomment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
	reason=models.CharField(max_length=2000)
	created = models.DateTimeField(auto_now_add=True)
class Hidecomment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    comments=models.ManyToManyField(Comment,blank=True,related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
class Comment_emotions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='comment',null=True)
    emotion=models.CharField(max_length=10,choices=emotion_choice,null=True)
