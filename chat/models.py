from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from accounts.models import *
from post.models import *
import datetime
import uuid
from mimetypes import guess_type
import os
# Create your models here.
from datetime import timedelta
current_date=datetime.datetime.now()
yesterday=current_date-timedelta(days=1)

class Thread(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE,related_name='admin')
    group_name=models.CharField(max_length=200,null=True)
    image = models.ImageField(blank=True, upload_to="chat/")
    timestamp = models.DateTimeField(auto_now_add=True)
    group=models.BooleanField(default=False)
    participant=models.ManyToManyField(User,blank=True,related_name='participant')
    emoticon=models.CharField(max_length=200,default='like')
    theme=models.CharField(max_length=200,null=True)
    def count_message(self):
        return Message.objects.filter(thread=self).count()
    def message_last(self):
        if Message.objects.filter(message=self).exists():
            return Message.objects.filter(message=self).last()
    
notification_choice=(
    ('1',"Video"),
    ('2',"Message"),
    ('3',"All")
)
type_choice=(
    ('1',"text"),
    ('2',"image"),
    ('3',"file")
)
class Member(models.Model):
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE, related_name='member_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='member_user')
    nickname=models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    is_seen = models.BooleanField(default=True)
    turnoff=models.CharField(null=True,max_length=100)
    blocker=models.ManyToManyField(User,blank=True,related_name="blocker")
    ignore=models.BooleanField(default=True)
   

class UploadFile(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    upload_by=models.ForeignKey(User, on_delete=models.CASCADE)
    file=models.FileField(null=True,upload_to="chat/")
    file_name=models.CharField(max_length=200,null=True)
    image_preview=models.FileField(null=True,upload_to="chat/")
    duration=models.FloatField(null=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-upload_date']
    def upload_file(self):
        if self.file and hasattr(self.file,'url'):
            return self.file.url
    def file_preview(self):
        if self.image_preview and hasattr(self.image_preview,'url'):
            return self.image_preview.url
    def filetype(self):
        type_tuple = guess_type(self.file.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"
        else:
            return 'pdf'
    def filename(self):
        return os.path.basename(self.file.name)
class Sticker(models.Model):
    image=models.ImageField()
    date_created = models.DateTimeField(auto_now=True)
    parent_id=models.IntegerField(blank=True,null=True)
class Message(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='message_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    message = models.TextField(null=True)
    story=models.ForeignKey(Story, on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now=True)
    def get_story(self):
        if self.story:
            if self.story.created.timestamp()>=yesterday.timestamp():
                return self.story.fileupload.file.url
    def get_message_filetype(self):
        if Filechat.objects.filter(message=self).exists():
            return Filechat.objects.filter(message=self).first().get_filetype()
class Filechat(models.Model):
    message= models.ForeignKey(Message, on_delete=models.CASCADE,related_name='message_file')
    upload_by=models.ForeignKey(User, on_delete=models.CASCADE)
    file=models.FileField(upload_to="chat/")
    file_name=models.CharField(max_length=200,null=True)
    file_preview=models.FileField(null=True,upload_to="chat/")
    duration=models.FloatField(default=0)
    upload_date=models.DateTimeField(auto_now_add=True)
    def upload_file(self):
        if self.file and hasattr(self.file,'url'):
            return self.file.url
    def get_file_preview(self):
        if self.file_preview and hasattr(self.file_preview,'url'):
            return self.file_preview.url
    def get_filetype(self):
        type_tuple = guess_type(self.file.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"
        else:
            return 'pdf'
    def filename(self):
        return os.path.basename(self.file.name)

   

