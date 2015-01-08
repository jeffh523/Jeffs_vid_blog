import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<secret key>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


ALLOWED_HOSTS = []				# enter domains for production


# Application definition

ADMINS = (
	('Jeff H', 'jeffh523@gmail.com'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'Blog',
	'south',						
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Project1.urls'

WSGI_APPLICATION = 'Project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
	
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 			# backends.postgresql_psycopg2 for production
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),		# 'blog_db',  for production
		#'USER': '',										# fill out for production
		#'PASSWORD': '',									# fill out for production
		#'HOST': '',										# uncomment for production
		#'PORT': '',										# uncomment for production
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_ROOT = '/home/jeffh523/webapps/static_media/'     # uncomment for production

STATIC_URL = '/static/'

# Uncomment the below for production:
"""
STATICFILES_DIRS = (
    '/home/jeffh523/webapps/blog/Project1/Blog/static',								
)
"""
