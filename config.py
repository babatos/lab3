import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL = "lab2serverdatabase.postgres.database.azure.com"
    POSTGRES_USER = "ducpm34@lab2serverdatabase"
    POSTGRES_PW = "Jamepotterbg998@"
    POSTGRES_DB = "techconfdb"
    DB_URL = "postgresql://{user}:{pw}@{url}/{db}".format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = "Endpoint=sb://lab3servicebusnamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=fGo28jt7QWg6BMHL4Imp90DhFDtza3X/u+ASbCTOTFI="
    SERVICE_BUS_QUEUE_NAME = "notificationqueue"
    ADMIN_EMAIL_ADDRESS: "info@techconf.com"
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False