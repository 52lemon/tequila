# -*- coding: utf-8 -*-

import os

DOMAIN = 'http://127.0.0.1:8000'

DEFAULT_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'pics')


SETTINGS = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'cookie_secret': 'ee93be7b3b08f4d0f31d16240d352b777f687e57',
    'login_url': '/auth/login',
    'xsrf_token': True,
    'debug': False
}


DATABASE = {
    'default': {
        'host': 'localhost',
        'port': 3306,
        'database': 'tequila',
        'user': 'root',
        'password': 'woaini',
        'charset': 'utf8'
    }
}


REDIS = {
    'default': {
        'host': 'localhost',
        'port': 6379,
        'password': '',
        'selected_db': 0,
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": os.path.join(os.path.dirname(__file__), 'tequila.log'),
            'mode': 'w+',
            "maxBytes": 1024*1024*5,  # 5 MB
            "backupCount": 20,
            "encoding": "utf8"
        },
        "admin": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": os.path.join(os.path.dirname(__file__), 'admin.log'),
            'mode': 'w+',
            "maxBytes": 1024*1024*2,  # 5 MB
            "backupCount": 20,
            "encoding": "utf8"
        },
    },

    "loggers": {
        "console": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": "no"
        },
        "file": {
            "level": "INFO",
            "handlers": ["file"],
            "porpagate": "no"
        },
        "admin": {
            "level": "INFO",
            "handlers": ["admin"],
            "porpagate": "no"
        }
    },
}