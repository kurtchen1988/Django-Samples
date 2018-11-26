SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/MyDjango'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

request.session['k1']

request.session.get['k1','']

request.session.setdefault('k1','')

request.session['k1'] = 123

del request.session['k1']

request.session.clear()

request.session.keys()

request.session.values()

request.session.session_key