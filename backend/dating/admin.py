from django.contrib import admin
from .models import Profile, Like, Match, Conversation, Message, Report, Block
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Match)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Report)
admin.site.register(Block)
