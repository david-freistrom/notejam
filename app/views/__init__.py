from flask_login import LoginManager

def init_app(app):
    print("app.views.__init__.init_app()")

    login_manager = LoginManager()
    login_manager.login_view = "signin"
    login_manager.init_app(app)

    with app.app_context():

        from . import notes
        from . import pads
        from . import auth
        from . import home
        from . import views