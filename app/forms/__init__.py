def init_app(app):
    print("app.forms.__init__.init_app()")

from .notes import NoteForm
from .pads import PadForm
from .auth import SigninForm, SignupForm, ChangePasswordForm, ForgotPasswordForm
from .forms import DeleteForm
        
__all__ = [NoteForm, PadForm, SigninForm, SignupForm, ChangePasswordForm, ForgotPasswordForm, DeleteForm]