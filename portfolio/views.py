from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse, Http404
from django.conf import settings
import os
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
    
    # Sort certifications in the user's requested order
    cert_order = [
        "Python Full Stack Training",
        "Problem Solving (Intermediate)",
        "Certificate of Merit - Debugging",
        "Web Development Internship",
        "Diploma in Computer Application",
        "National Level IT Symposium – SAIT'23",
        "Project Completion Certificate",
        "Inplant Training - MEM Development",
        "Artificial Intelligence Workshop"
    ]
    certifications = list(Certification.objects.all())
    certifications.sort(key=lambda c: cert_order.index(c.title) if c.title in cert_order else len(cert_order))
    
    context = {
        'projects': projects,
        'skills': skills,
        'certifications': certifications,
    }
    return render(request, 'portfolio/index.html', context)


def download_resume(request):
    """Serve the resume file as a forced download (works for PDF, DOCX, etc.)"""
    # Look in the app's static folder
    resume_path = os.path.join(
        settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'resume', 'Saritha_N_PythonFullStack.pdf'
    )
    if not os.path.exists(resume_path):
        raise Http404("Resume file not found.")

    response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Saritha_N_Resume.pdf"'
    return response

