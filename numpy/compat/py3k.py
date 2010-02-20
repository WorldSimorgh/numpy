"""
Python 3 compatibility tools.

"""

__all__ = ['bytes', 'asbytes', 'isfileobj', 'getexception', 'strchar',
           'unicode', 'asunicode', 'asbytes_nested', 'asunicode_nested']

import sys

if sys.version_info[0] >= 3:
    import io
    bytes = bytes
    unicode = str
    asunicode = str
    def asbytes(s):
        if isinstance(s, bytes):
            return s
        return s.encode('iso-8859-1')
    def isfileobj(f):
        return isinstance(f, io.IOBase)
    strchar = 'U'
else:
    bytes = str
    unicode = unicode
    asbytes = str
    strchar = 'S'
    def isfileobj(f):
        return isinstance(f, file)
    def asunicode(s):
        if isinstance(s, unicode):
            return s
        return s.decode('iso-8859-1')

def getexception():
    return sys.exc_info()[1]

def asbytes_nested(x):
    if hasattr(x, '__iter__') and not isinstance(x, (bytes, unicode)):
        return [asbytes_nested(y) for y in x]
    else:
        return asbytes(x)

def asunicode_nested(x):
    if hasattr(x, '__iter__') and not isinstance(x, (bytes, unicode)):
        return [asunicode_nested(y) for y in x]
    else:
        return asunicode(x)
