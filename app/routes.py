from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_mail import Message
from app.models import User, Contact, Project, Certificate
from app import db, mail
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/images/project-images')
CERT_IMAGE_FOLDER = os.path.join(os.getcwd(),  'app/static/images/certificate-images')
CERT_PDF_FOLDER = os.path.join(os.getcwd(),  'app/static/certificates')

@main.route('/')
def home():
    user = User.query.first()
    projects = Project.query.order_by(Project.id.desc()).all()
    certificates = Certificate.query.all()
    return render_template('index.html', user=user, projects=projects, certificates=certificates)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['POST'])
def contact():
    name = request.form['fullname']
    email = request.form['email']
    number = request.form['number']
    subject = request.form['subject']
    message = request.form['message']

    new_contact = Contact(name=name, email=email, number=number, subject=subject, message=message)
    db.session.add(new_contact)
    db.session.commit()

    # This SEnd Email
    msg = Message(
        subject=f"Portfolio Contact: {subject}",
        recipients=[os.getenv("MAIL_USERNAME")]
    )

    msg.body = f"""
New Message from your portfolio

Name: {name}
Email: {email}
Phone:{number}

Message:
{message}
    """

    mail.send(msg)

    return redirect(url_for('main.home'))

@main.route('/add-project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        github = request.form['github']
        demo = request.form['demo']

        # handle file upload
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        new_project = Project(
            title=title,
            description=description,
            github_link=github,
            live_demo=demo,
            image_filename=filename
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_project.html')

@main.route('/add-certificate', methods=['GET', 'POST'])
def add_certificate():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        image = request.files['image']
        pdf = request.files['pdf']

        image_filename = secure_filename(image.filename)
        pdf_filename = secure_filename(pdf.filename)

        image.save(os.path.join(CERT_IMAGE_FOLDER, image_filename))
        pdf.save(os.path.join(CERT_PDF_FOLDER, pdf_filename))

        new_cert = Certificate(
            title=title,
            description=description,
            image_filename=image_filename,
            pdf_filename=pdf_filename
        )

        db.session.add(new_cert)
        db.session.commit()

        return redirect(url_for('main.home'))
    
    return render_template('add_certificate.html')