from .settings import *


# static files and static root settings changed for production
del STATICFILES_DIRS

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

