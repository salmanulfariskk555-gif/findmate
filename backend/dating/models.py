from django.conf import settings
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    GENDER_CHOICES = [('woman','Woman'),('man','Man'),('nonbinary','Non-binary'),('prefer_not_to_say','Prefer not to say')]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField()
    display_name = models.CharField(max_length=80, blank=True)
    gender = models.CharField(max_length=24, choices=GENDER_CHOICES, blank=True)
    interested_in = models.CharField(max_length=24, blank=True)
    city = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    interests = models.JSONField(default=list, blank=True)
    photo_url = models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.display_name or self.user.username

class Like(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_likes')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['sender','receiver'], name='unique_like_pair')]

class Match(models.Model):
    user_one = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_one')
    user_two = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_two')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user_one','user_two'], name='unique_match_pair')]

class Conversation(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

class Report(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_made')
    reported_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_received')
    reason = models.CharField(max_length=80)
    details = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Block(models.Model):
    blocker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blocks_made')
    blocked = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blocks_received')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['blocker','blocked'], name='unique_block_pair')]
