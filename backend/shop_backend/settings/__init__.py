from .base import *


if os.environ.get('DJANGO_ENV') == 'dev':
    from .development import *
else:
    from .production import *
