import os


class Config():
    SECRET_KEY = 'V579RO6FYUYV'
    MONGODB_DB = 'flaskblog'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017

    SECURITY_REGISTERABLE = True
    SECURITY_USERNAME_ENABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    #for offline testing during user registration
    SECURITY_EMAIL_VALIDATOR_ARGS = {
        "check_deliverability": False
    }
    SECURITY_PASSWORD_LENGTH_MIN = 4
    SECURITY_PASSWORD_SALT = "128991772686469037771319591084936354264"
    SECURITY_CHANGEABLE = True

    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

    # DEBUG_TB_PANELS = ('flask_mongoengine.panels.MongoDebugPanel')
    # DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    # DEBUG_TB_PROFILER_ENABLED = True
