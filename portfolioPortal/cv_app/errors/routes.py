

from flask import Blueprint, render_template


errors_bp = Blueprint('errors', __name__, template_folder='templates')


@errors_bp.app_errorhandler(404)
def error_404(error):
    title = "404 Error"

    return render_template('errors/404.html', title=title)


@errors_bp.app_errorhandler(403)
def error_403(error):
    title = "403 Error"

    return render_template('errors/403.html', title=title)


@errors_bp.app_errorhandler(500)
def error_500(error):
    title = "500 Error"

    return render_template('errors/500.html', title=title)
