
from flask import Blueprint, render_template


about_bp = Blueprint('about', __name__, template_folder='templates')


@about_bp.route('/experience')
def experience():
    title = 'Work Experience'

    return render_template('experience.html', title=title)


@about_bp.route('/bio')
def bio():
    title = 'About Me'

    return render_template('bio.html', title=title)


@about_bp.route('/resume')
def resume():
    title = 'Resume'

    return render_template('resume.html', title=title)
