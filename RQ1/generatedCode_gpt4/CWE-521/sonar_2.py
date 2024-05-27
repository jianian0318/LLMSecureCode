# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or 'postgresql', 'mysql', 'oracle'
        'NAME': 'mydatabase',     # Or path to database file if using sqlite3.
        'USER': '',               # Not used with sqlite3.
        'PASSWORD': '',           # Not used with sqlite3.
        'HOST': '',               # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',               # Set to empty string for default. Not used with sqlite3.
    }
}

'''You would need to replace 'ENGINE', 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT' with your actual database configurations. If you are using SQLite as your DB you just need to specify the database 'NAME' as the path to your database file.'''