from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6j%p=0g_p5fnejnp^blb4u=ej+qrawa(=$nrr-jg-$^bdlc%99'




try:
    from .local import *
except ImportError:
    pass
