from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt     # to password convert into hash 

# Config class
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize the database and migration objects
db = SQLAlchemy()   # make instance
migrate = Migrate() # make instance
bcrypt = Bcrypt()   # make instance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database and migrations with the app
    db.init_app(app)    # Initialize database
    migrate.init_app(app, db)   # Initialize migrations
    bcrypt.init_app(app)    # Initialize bcrypt passwoprd hasher
    
    # Register blueprints routes
    from auth_app.views import user_auth
    app.register_blueprint(user_auth, url_prefix='/')     # resgiter User_app blueprint route
    
    return app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
