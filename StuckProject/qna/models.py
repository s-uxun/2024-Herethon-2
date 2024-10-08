from django.db import models
from quiz.models import *
from django.contrib.auth.models import User


class QuestionRoom(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="question_rooms")
    title = models.CharField(max_length=30)
    folder = models.ForeignKey(to=Folder, on_delete=models.CASCADE,related_name="qnas")
    file = models.FileField(upload_to="file/%Y/%m/%d/")
    memo = models.CharField(max_length=10000, blank=True)
    created_at = models.DateField(auto_now_add=True)


class Chat(models.Model):
    question_room = models.ForeignKey(to=QuestionRoom, on_delete=models.CASCADE, related_name="chats")
    user_chat = models.CharField(max_length=100)
    gpt_chat = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
