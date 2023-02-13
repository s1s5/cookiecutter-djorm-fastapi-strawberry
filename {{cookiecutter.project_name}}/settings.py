import datetime

import environ


env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, r"a/qX:bn<hDcmm>Y<ow!PbX+B<%-StL)t[G\L_VZ1&p@$!zCVE"),
)

ROOT_URLCONF = "{{cookiecutter.project_name}}.urls"
DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    "default": env.db(default="sqlite://:memory:"),
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
TZ_INFO = datetime.timezone(datetime.timedelta(hours=9))
USE_TZ = True

INSTALLED_APPS = ["{{cookiecutter.project_name}}"]
