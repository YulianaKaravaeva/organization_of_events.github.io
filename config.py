class Config(object):
  # Определяет, включен ли режим отладки
  # В случае если включен, flask будет показывать
  # подробную отладочную информацию. Если выключен -
  # - 500 ошибку без какой либо дополнительной информации.
  DEBUG = False
  FLASK_APP="src"
  
  # Включение защиты против "Cross-site Request Forgery (CSRF)"
  CSRF_ENABLED = True
  
  # Случайный ключ, которые будет исползоваться для подписи
  # данных, например cookies.
  SECRET_KEY = 'RANDOM_SECRET_KEY'
  SECURITY_PASSWORD_SALT = "cefcefe"
      
  # URI используемая для подключения к базе данных
  # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  SQLALCHEMY_DATABASE_URI = 'sqlite:///new_org_events.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # Необходимые настройки для работы с почтой
  MAIL_SERVER = "smtp.googlemail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = "organization.events.email@gmail.com"
  MAIL_PASSWORD = "dojs zrxc cxko xtrk"
  MAIL_DEFAULT_SENDER = "organization.events.email@gmail.com"



class ProductionConfig(Config):
  DEBUG = False

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True