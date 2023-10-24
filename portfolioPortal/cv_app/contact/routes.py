
from database import db
from flask import url_for, render_template, redirect, request, flash, Blueprint
from cv_app.contact.models import ContactFormModel
from cv_app.contact.forms import ContactForm
from cv_app.contact.utils import send_contact_email, send_reply_email

import os


contact_bp = Blueprint('contact', __name__, template_folder='templates')


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    title = "Contact Me"
    contact_form = ContactForm()

    if request.method == 'POST' and contact_form.validate_on_submit():
        users_email = contact_form.email.data
        name = contact_form.name.data
        company = contact_form.company.data
        email = contact_form.email.data
        subject = contact_form.subject.data
        users_message = contact_form.content.data

        new_contact = ContactFormModel(
            name=name,
            company=company,
            email=email,
            subject=subject,
            content=users_message
        )
        db.session.add(new_contact)
        db.session.commit()
        send_contact_email(name, company, email, subject, users_message)
        send_reply_email(name, email, company)

        flash('Your message has been recorded and an automated confirmation email has been sent.', 'success')
        return redirect(url_for('main.home'))

    return render_template('contact.html', title=title,
                           form=contact_form)
