from django.conf import settings
from django.db import models
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="match_profile")
    display_name=models.CharField(max_length=80)
    birth_date=models.DateField()
    city=models.CharField(max_length=100,blank=True)
    bio=models.TextField(max_length=600,blank=True)
    interests=models.CharField(max_length=300,blank=True)
    visible=models.BooleanField(default=False)
    approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.display_name
class Like(models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="likes_sent")
    recipient=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="likes_received")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["sender","recipient"],name="unique_like")]
class Block(models.Model):
    blocker=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="blocks_made")
    blocked=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="blocks_received")
    class Meta:
        constraints=[models.UniqueConstraint(fields=["blocker","blocked"],name="unique_block")]
class Report(models.Model):
    reporter=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="reports_made")
    reported=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="reports_received")
    reason=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
