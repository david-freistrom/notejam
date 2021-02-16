from flask import current_app
from flask_login import (login_user, login_required, logout_user, current_user)
from flask import render_template, flash, redirect, url_for
import hashlib, logging
from datetime import date
from flask_mail import Message

from app import mail
from ..models import User, db
from ..forms import (SigninForm, SignupForm, ChangePasswordForm, ForgotPasswordForm)


@current_app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@current_app.route('/settings/', methods=['GET', 'POST'])
@login_required
def account_settings():
  form = ChangePasswordForm(user=current_user)
  if form.validate_on_submit():
      current_user.set_password(form.new_password.data)
      db.session.commit()
      flash("Your password is successfully changed.", 'success')
      return redirect(url_for('home'))
  return render_template('users/settings.html', form=form)


@current_app.route('/forgot-password/', methods=['GET', 'POST'])
def forgot_password():
  form = ForgotPasswordForm()
  if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      new_password = _generate_password(user)
      user.set_password(new_password)

      message = Message(
          subject="Notejam password",
          body="Your new password is {}".format(new_password),
          sender="from@notejamapp.com",
          recipients=[user.email]
      )
      mail.send(message)

      db.session.commit()
      flash("Find new password in your inbox", 'success')
      return redirect(url_for('home'))
  return render_template('users/forgot_password.html', form=form)


# @TODO use macro for form fields in template
@current_app.route('/signin/', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
  if form.validate_on_submit():
      auth_user = User.authenticate(form.email.data, form.password.data)
      if auth_user:
          login_user(auth_user)
          flash('You are signed in!', 'success')
          return redirect(url_for('home'))
      else:
          flash('Wrong email or password', 'error')
  return render_template('users/signin.html', form=form)


@current_app.route('/signout/')
def signout():
  logout_user()
  return redirect(url_for('signin'))


@current_app.route('/signup/', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
      user = User(email=form.email.data)
      user.set_password(form.password.data)
      db.session.add(user)
      db.session.commit()
      flash('Account is created. Now you can sign in.', 'success')
      return redirect(url_for('signin'))
  return render_template('users/signup.html', form=form)


def _generate_password(user):
  ''' generate new user password '''
  m = hashlib.md5()
  m.update(
    "{email}{secret}{date}".format(
        email=user.email,
        secret=current_app.secret_key,
        date=str(date.today())
  ).encode('utf-8'))
  return m.hexdigest()[:8]