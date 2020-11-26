from .default import Config

# setting for development staging
class Development(Config):
    DEBUG=True
    ENV='development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/klinikmanage'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
