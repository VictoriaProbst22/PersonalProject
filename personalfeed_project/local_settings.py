# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c_pw-j^&qc0aqb3cjmt(3e34(z7xw!wh#py^x_65w50*yki-tk'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'personalfeed_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'PASSword2022'
    }
}
