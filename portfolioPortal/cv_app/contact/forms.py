
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    company = StringField('Company', render_kw={"placeholder": "NASA Hopefully?"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "example@gmail.com"})
    subject = SelectField('Subject', choices=[
        ('', 'Select a Subject'),
        ('general_inquiry', 'General Inquiry'),
        ('collaboration_opportunity', 'Collaboration Opportunity'),
        ('job_opportunity', 'Job Opportunity'),
        ('feedback_opportunity', 'Feedback on Portfolio/Projects'),
        ('support_opportunity', 'Technical Support'),
        ('speaking_opportunity', 'Speaking Engagement'),
        ('mentorship_opportunity', 'Mentorship Request'),
        ('media_opportunity', 'Press/Media Inquiry'),
        ('other', 'Other'),
    ], validators=[DataRequired()])
    content = TextAreaField('Message Content', validators=[DataRequired()],
                            render_kw={"placeholder": "Your Message"})
    checkbox = BooleanField('I recognize the building on the home page.')
    submit = SubmitField('Submit')
