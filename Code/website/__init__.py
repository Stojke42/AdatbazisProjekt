from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sometingsecretkey"

    from .view import views
    from .auth import auth

    app.register_blueprint(views, url_prefic="/")
    app.register_blueprint(auth, url_prefic="/")

    from .models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from website import dbapp
    @login_manager.user_loader
    def load_user(id):
         return dbapp.backuser(id)

    return app
