from __future__ import absolute_import, unicode_literals

from .base import *
SECRET_KEY = '6j%p=0g_p2fnejnp^blb4u=ej+qrawa(=$nrr-jg-$^bdlc%99'
ALLOWED_HOSTS = ['rost23.ru', 'www.rost23.ru']
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
