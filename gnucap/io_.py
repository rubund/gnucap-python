# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_io_')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_io_')
    _io_ = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_io_', [dirname(__file__)])
        except ImportError:
            import _io_
            return _io_
        try:
            _mod = imp.load_module('_io_', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _io_ = swig_import_helper()
    del swig_import_helper
else:
    import _io_
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class OMSTREAM(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OMSTREAM, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OMSTREAM, name)
    __repr__ = _swig_repr

    def __init__(self, f=None):
        this = _io_.new_OMSTREAM(f)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def attach(self, *args):
        return _io_.OMSTREAM_attach(self, *args)

    def detach(self, *args):
        return _io_.OMSTREAM_detach(self, *args)

    def __sub__(self, y):
        return _io_.OMSTREAM___sub__(self, y)

    def __add__(self, y):
        return _io_.OMSTREAM___add__(self, y)

    def any(self):
        return _io_.OMSTREAM_any(self)

    def cipher(self):
        return _io_.OMSTREAM_cipher(self)

    def pack(self):
        return _io_.OMSTREAM_pack(self)

    def format(self):
        return _io_.OMSTREAM_format(self)

    def setcipher(self, x=True):
        return _io_.OMSTREAM_setcipher(self, x)

    def setpack(self, x=True):
        return _io_.OMSTREAM_setpack(self, x)

    def setfloatwidth(self, d, w=0):
        return _io_.OMSTREAM_setfloatwidth(self, d, w)

    def setformat(self, f):
        return _io_.OMSTREAM_setformat(self, f)

    def reset(self):
        return _io_.OMSTREAM_reset(self)

    def tab(self, *args):
        return _io_.OMSTREAM_tab(self, *args)

    def form(self, arg2):
        return _io_.OMSTREAM_form(self, arg2)

    def __lshift__(self, *args):
        return _io_.OMSTREAM___lshift__(self, *args)

    def _print(self, s):
        return _io_.OMSTREAM__print(self, s)
    __swig_destroy__ = _io_.delete_OMSTREAM
    __del__ = lambda self: None
OMSTREAM_swigregister = _io_.OMSTREAM_swigregister
OMSTREAM_swigregister(OMSTREAM)
cvar = _io_.cvar
MAXHANDLE = cvar.MAXHANDLE


def octal(x):
    return _io_.octal(x)
octal = _io_.octal
class IO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IO, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mstdout"] = _io_.IO_mstdout_set
    __swig_getmethods__["mstdout"] = _io_.IO_mstdout_get
    if _newclass:
        mstdout = _swig_property(_io_.IO_mstdout_get, _io_.IO_mstdout_set)
    __swig_setmethods__["error"] = _io_.IO_error_set
    __swig_getmethods__["error"] = _io_.IO_error_get
    if _newclass:
        error = _swig_property(_io_.IO_error_get, _io_.IO_error_set)
    __swig_setmethods__["plotout"] = _io_.IO_plotout_set
    __swig_getmethods__["plotout"] = _io_.IO_plotout_get
    if _newclass:
        plotout = _swig_property(_io_.IO_plotout_get, _io_.IO_plotout_set)
    __swig_setmethods__["plotset"] = _io_.IO_plotset_set
    __swig_getmethods__["plotset"] = _io_.IO_plotset_get
    if _newclass:
        plotset = _swig_property(_io_.IO_plotset_get, _io_.IO_plotset_set)
    __swig_setmethods__["formaat"] = _io_.IO_formaat_set
    __swig_getmethods__["formaat"] = _io_.IO_formaat_get
    if _newclass:
        formaat = _swig_property(_io_.IO_formaat_get, _io_.IO_formaat_set)
    __swig_setmethods__["incipher"] = _io_.IO_incipher_set
    __swig_getmethods__["incipher"] = _io_.IO_incipher_get
    if _newclass:
        incipher = _swig_property(_io_.IO_incipher_get, _io_.IO_incipher_set)

    def __init__(self):
        this = _io_.new_IO()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _io_.delete_IO
    __del__ = lambda self: None
IO_swigregister = _io_.IO_swigregister
IO_swigregister(IO)


def initio(arg1):
    return _io_.initio(arg1)
initio = _io_.initio

def outreset():
    return _io_.outreset()
outreset = _io_.outreset

def outset(arg1, arg2):
    return _io_.outset(arg1, arg2)
outset = _io_.outset

def findfile(arg1, arg2, arg3):
    return _io_.findfile(arg1, arg2, arg3)
findfile = _io_.findfile

def xclose(arg1):
    return _io_.xclose(arg1)
xclose = _io_.xclose

def xopen(arg1, arg2, arg3):
    return _io_.xopen(arg1, arg2, arg3)
xopen = _io_.xopen
# This file is compatible with both classic and new-style classes.

