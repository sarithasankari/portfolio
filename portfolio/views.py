from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Certification, ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')

    projects = Project.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
        'certifications': certifications,
    }
    return render(request, 'portfolio/index.html', context)
