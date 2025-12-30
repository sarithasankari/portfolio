from django.contrib import admin
from .models import Project, Skill, Certification, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(ContactMessage)
