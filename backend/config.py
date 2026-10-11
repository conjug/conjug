import os


def get_bool_env(var_name, default=True):
    val = os.getenv(var_name)
    if val is None:
        return default
    elif val == "True":
        return True
    return False


# Also the salt of the stored password hashes: rotating it invalidates them.
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')

DATABASE = os.getenv('MYSQL_DATABASE', 'name_db')
USER = os.getenv('MYSQL_USER', 'user')
PASSWORD = os.getenv('MYSQL_PASSWORD', 'user_password')
PORT = os.getenv('DB_PORT', '3306')

SQLALCHEMY_DATABASE_URI = (
    f"mariadb+mariadbconnector://{USER}:{PASSWORD}@mariadb:{PORT}/{DATABASE}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = get_bool_env('TRACK_MODIFICATIONS', False)

SESSION_COOKIE_HTTPONLY = get_bool_env('COOKIE_HTTPONLY', True)
SESSION_COOKIE_SECURE = get_bool_env('COOKIE_SECURE', True)
SESSION_COOKIE_SAMESITE = os.getenv('COOKIE_SAMESITE', 'None')
PERMANENT_SESSION_LIFETIME = int(os.getenv('LIFETIME', 86400))
SESSION_PERMANENT = get_bool_env('PERMANENT', True)
