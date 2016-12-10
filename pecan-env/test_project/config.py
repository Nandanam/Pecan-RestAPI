# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'test_project.controllers.root.RootController',
    'modules': ['test_project'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/test_project/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

MySQLdb = {
         'url' : 'mysql+mysqldb://root:root@localhost/uni300?charset=utf8&use_unicode=0',
         'echo' : False,
         'echo_pool' :False,
         'pool_recycle' : 3600,
         'encoding' : 'utf-8'
}
#sqlalchemy = {
	#'url'	:'mysql+mysqldb://root:root@localhost/uni300?charset=utf8&use_unicode=0',
	#'url'   : 'sqlite:///localhost',
       # 'echo'  : False,
	#'echo_pool': False,
	#'pool_recycle' : 3600,
	#'encoding'	: 'utf-8'
#}


logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'test_project': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'pecan': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
        '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
