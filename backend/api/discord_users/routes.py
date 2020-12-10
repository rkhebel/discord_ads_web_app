from flask import current_app as app
from flask import Blueprint, render_template, url_for, redirect, flash, request, session
from ..forms import LoginForm, SignupForm
from ..models import db, User
from .. import login_manager
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
discord_users = Blueprint(
    'discord_users', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/discord_users'
)

@discord_users.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit(): #this happens if its a post and the user clicked submit and it was validated
        existing_user = User.query.filter_by(email=form.email.data, user_type='discord_user').first()
        if existing_user is None:
            user = User(
                first_name=form.firstName.data,
                last_name=form.lastName.data,
                email=form.email.data,
                user_type='discord_user'
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('discord_users.home'))
        flash('A user already exists with that email address.')
    return render_template( #basically if it was a GET or form failed to validate
        'signup.jinja2',
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )


@discord_users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('discord_users.home'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, user_type='discord_user').first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('discord_users.home'))
        flash('Invalid username/password combination')
        return redirect(url_for('discord_users.login'))
    return render_template(
        'login.jinja2',
        form=form,
        title='Log in.',
        template='login-page',
        body="Log in with your User account."
    )


@discord_users.route('/', methods=['GET'])
@login_required
def home():
    return None