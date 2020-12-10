from flask import current_app as app
from flask import render_template, url_for, redirect, flash, request, session
from .forms import LoginForm, SignupForm
from .models import db, User
from . import login_manager
from flask_login import current_user, login_required, logout_user

# @app.errorhandler(404)
# def not_found():
#     return some generic page here


@app.route('/')
def home():
    return render_template(
        'home.jinja2',
        title = 'Discord Ads',
        description = 'The only way to advertise on Discord!'
        )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('login'))