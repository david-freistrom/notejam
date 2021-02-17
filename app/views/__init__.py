def init_app(app):
    print("app.views.__init__.init_app()")

    with app.app_context():

        from . import notes
        from . import pads
        from . import auth
        from . import home
        from . import views