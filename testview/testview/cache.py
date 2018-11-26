CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':[
			'172.19.26.240:11211',
			'172.19.26.242:11211',
		]
	}
}

CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.db.DatabaseCache',
		'LOCATION':'my_cache_table',
	}
}

CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.fileBased.FileBasedCache',
		'LOCATION':'/django_cache',
	}
}

CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.locmen.LocMemCache',
		'LOCATION':'unique-snowflake',
	}
}

CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.dummy.DummyCache',
	}
}

CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.db.DatabaseCache',
		'LOCATION':'my_cache_table',
		'TIMEOUT':60,
	'OPTIONS':{
		'MAX_ENTRIES':1000,
		'CULL_FREQUENCY':3,
	}
},
	'MyDjango':{
		'BACKEND':'django.core.cache.backends.db.DatabaseCache',
		'LOCATION':'MyDjango_cache_table',
	}
}

MIDDLEWARE = [
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',

	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',

	'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_SECONDS = 15

CACHE_MIDDLEWARE_ALIAS = 'default'

CACHE_MIDDLEWARE_KEY_PREFIX = 'MyDjango'