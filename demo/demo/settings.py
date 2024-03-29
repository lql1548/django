"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目的根目录，方便开发人员使用
# os.path.abspath 绝对路径
# os.path.dirname 文件所在目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 秘钥
SECRET_KEY = 'x%u4o$uhmzkq)!52++p^mo*mrugardf2s0jpq55rvs#!bl$poz'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
# True 开启调试模式
# 开启调试模式： 1.更改django代码，自动重启服务 2.显示错误信息，请求信息
DEBUG = True

# 允许访问的主机
ALLOWED_HOSTS = ["*"]


# Application definition

# 注册app  注册子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]

# 中间件 中间人
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 路由的根目录
ROOT_URLCONF = 'demo.urls'

# 模板的配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', ## django模板引擎
        'DIRS': [os.path.join(BASE_DIR,"templates")],  ## 配置模板目录路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# django内置服务器
WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库相关的配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'demo',  ## 库名
        'USER':'root',  ## 用户名
        'PASSWORD':'123456',  ## 密码
        'HOST':'127.0.0.1',  ## 主机 IP
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# 权限认证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 语言
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'zh-hans'  # 中文

# 失去
TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Shanghai'  # 上海时区

# 翻译系统
USE_I18N = True

# 数据本地化配置
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 静态文件的配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),  ## 静态文件的路径  地址
)
