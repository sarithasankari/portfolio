import os
import django
from django.core.files import File
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project, Skill, Certification

def populate():
    # Define Base Path for Static Images
    base_dir = Path(__file__).resolve().parent
    static_img_dir = base_dir / 'portfolio' / 'static' / 'portfolio' / 'images'

    print("Populating Projects...")
    projects = [
        {
            'title': "Roadside Assistance Platform",
            'description': "A comprehensive web application connecting users with roadside service providers for emergency vehicle assistance, towing, and repair services.",
            'image_name': "road.jpg",
            'tags': "HTML, CSS, JavaScript, Django",
            'link': "https://github.com/sarithasankari/Roadside-Assistance"
        },
        {
            'title': "Online Shopping Website",
            'description': "A fully functional e-commerce website with product listings, shopping cart, and checkout functionality.",
            'image_name': "one.jpg",
            'tags': "HTML, CSS, JavaScript",
            'link': "https://sarithann.neocities.org/shop/shopping/"
        },
        {
            'title': "Movie Search App",
            'description': "A dynamic movie search application that fetches data from an API and displays movie details, posters, and ratings.",
            'image_name': "mov.jpg",
            'tags': "HTML, CSS, JavaScript",
            'link': "https://sarithann.neocities.org/movie1/movie/id"
        }
    ]

    for p_data in projects:
        project, created = Project.objects.update_or_create(
            title=p_data['title'],
            defaults={
                'description': p_data['description'],
                'tags': p_data['tags'],
                'link': p_data['link']
            }
        )
        if created:
            img_path = static_img_dir / p_data['image_name']
            if img_path.exists():
                with open(img_path, 'rb') as f:
                    project.image.save(p_data['image_name'], File(f), save=True)
            print(f"Created Project: {project.title}")
        else:
            print(f"Project already exists: {project.title}")

    print("\nPopulating Skills...")
    # Categories: 'FE': Frontend, 'BE': Backend, 'DB': Database
    skills = [
        {'name': "HTML5", 'proficiency': 95, 'category': 'FE', 'icon_class': "fab fa-html5"},
        {'name': "CSS3", 'proficiency': 90, 'category': 'FE', 'icon_class': "fab fa-css3-alt"},
        {'name': "JavaScript", 'proficiency': 85, 'category': 'FE', 'icon_class': "fab fa-js"},
        {'name': "Bootstrap", 'proficiency': 80, 'category': 'FE', 'icon_class': "fab fa-bootstrap"},
        {'name': "Python", 'proficiency': 85, 'category': 'BE', 'icon_class': "fab fa-python"},
        {'name': "Django", 'proficiency': 70, 'category': 'BE', 'icon_class': "devicon-django-plain"},
        {'name': "PHP", 'proficiency': 75, 'category': 'BE', 'icon_class': "fab fa-php"},
        {'name': "MySQL", 'proficiency': 85, 'category': 'DB', 'icon_class': "fas fa-database"},
        {'name': "Git & GitHub", 'proficiency': 80, 'category': 'DB', 'icon_class': "fab fa-git-alt"},
        {'name': "VS Code", 'proficiency': 90, 'category': 'DB', 'icon_class': "fas fa-code"},
    ]

    for s_data in skills:
        skill, created = Skill.objects.get_or_create(
            name=s_data['name'],
            defaults=s_data
        )
        if created:
            print(f"Created Skill: {skill.name}")
        else:
            print(f"Skill already exists: {skill.name}")


    print("\nPopulating Certifications...")
    certs = [
        {
            'title': "Certificate of Merit - Debugging",
            'description': "Awarded Second Place in Debugging competition at Government Arts College, Dharmapuri.",
            'period': "Mar 2023",
            'image_name': "cr7.jpg"
        },
        {
            'title': "Python Full Stack Training",
            'description': 'Successfully completed Python Full Stack training program with Grade "A" from SLA.',
            'period': "Nov 2025",
            'image_name': "cr8.jpg"
        },
        {
            'title': "Web Development Internship",
            'description': "Successfully completed an internship in web development at CodeBind Technologies, Chennai.",
            'period': "May-June 2024",
            'image_name': "cr1.jpg"
        },
        {
            'title': "Artificial Intelligence Workshop",
            'description': "Participated in a one-day workshop on Artificial Intelligence at CodeBind Technologies, Chennai.",
            'period': "2024",
            'image_name': "cr2.jpg"
        },
        {
            'title': "Diploma in Computer Application",
            'description': "Completed Diploma in Computer Application with specialization in IT Fundamentals, Microsoft Office, and Python.",
            'period': "Aug-Nov 2023",
            'image_name': "cr3.jpg"
        },
        {
            'title': "Inplant Training - MEM Development",
            'description': "Underwent Inplant Training in MEM Development at CodeBind Technologies, Chennai.",
            'period': "June 2024",
            'image_name': "cr4.jpg"
        },
        {
            'title': "National Level IT Symposium – SAIT'23",
            'description': "Participated in the National Level IT Symposium organized by Sacred Heart College, Tirupattur.",
            'period': "Feb 2023",
            'image_name': "cr5.jpg"
        },
        {
            'title': "Project Completion Certificate",
            'description': 'Successfully completed the project "Online shopping website using HTML, CSS, JavaScript, PHP and MySQL" at CodeBind Technologies.',
            'period': "May-June 2024",
            'image_name': "cr6.jpg"
        },
    ]

    for c_data in certs:
        cert, created = Certification.objects.get_or_create(
            title=c_data['title'],
            defaults={
                'description': c_data['description'],
                'period': c_data['period']
            }
        )
        if created:
            img_path = static_img_dir / c_data['image_name']
            if img_path.exists():
                with open(img_path, 'rb') as f:
                    cert.image.save(c_data['image_name'], File(f), save=True)
            print(f"Created Certification: {cert.title}")
        else:
            print(f"Certification already exists: {cert.title}")

if __name__ == '__main__':
    populate()
