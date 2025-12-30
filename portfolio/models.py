from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    tags = models.CharField(max_length=200, help_text="Comma-separated tags")

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',')] if self.tags else []

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Percentage (0-100)")
    category = models.CharField(max_length=50, choices=[
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Database', 'Database & Tools'),
    ])
    icon_class = models.CharField(max_length=100, help_text="FontAwesome class e.g., 'fas fa-code'")

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='certifications/')
    period = models.CharField(max_length=100, help_text="e.g., May-June 2024")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
