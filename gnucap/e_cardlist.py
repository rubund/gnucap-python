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
        mname = '.'.join((pkg, '_e_cardlist')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_e_cardlist')
    _e_cardlist = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_e_cardlist', [dirname(__file__)])
        except ImportError:
            import _e_cardlist
            return _e_cardlist
        try:
            _mod = imp.load_module('_e_cardlist', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _e_cardlist = swig_import_helper()
    del swig_import_helper
else:
    import _e_cardlist
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


class CARD_LIST(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CARD_LIST, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CARD_LIST, name)
    __repr__ = _swig_repr

    def expand(self):
        return _e_cardlist.CARD_LIST_expand(self)

    def map_nodes(self):
        return _e_cardlist.CARD_LIST_map_nodes(self)

    def tr_iwant_matrix(self):
        return _e_cardlist.CARD_LIST_tr_iwant_matrix(self)

    def tr_begin(self):
        return _e_cardlist.CARD_LIST_tr_begin(self)

    def tr_restore(self):
        return _e_cardlist.CARD_LIST_tr_restore(self)

    def dc_advance(self):
        return _e_cardlist.CARD_LIST_dc_advance(self)

    def tr_advance(self):
        return _e_cardlist.CARD_LIST_tr_advance(self)

    def tr_regress(self):
        return _e_cardlist.CARD_LIST_tr_regress(self)

    def tr_needs_eval(self):
        return _e_cardlist.CARD_LIST_tr_needs_eval(self)

    def tr_queue_eval(self):
        return _e_cardlist.CARD_LIST_tr_queue_eval(self)

    def do_tr(self):
        return _e_cardlist.CARD_LIST_do_tr(self)

    def tr_load(self):
        return _e_cardlist.CARD_LIST_tr_load(self)

    def tr_review(self):
        return _e_cardlist.CARD_LIST_tr_review(self)

    def tr_accept(self):
        return _e_cardlist.CARD_LIST_tr_accept(self)

    def tr_unload(self):
        return _e_cardlist.CARD_LIST_tr_unload(self)

    def ac_iwant_matrix(self):
        return _e_cardlist.CARD_LIST_ac_iwant_matrix(self)

    def ac_begin(self):
        return _e_cardlist.CARD_LIST_ac_begin(self)

    def do_ac(self):
        return _e_cardlist.CARD_LIST_do_ac(self)

    def ac_load(self):
        return _e_cardlist.CARD_LIST_ac_load(self)

    def card_list_(self):
        return _e_cardlist.CARD_LIST_card_list_(self)

    def __init__(self):
        this = _e_cardlist.new_CARD_LIST()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_cardlist.delete_CARD_LIST
    __del__ = lambda self: None
CARD_LIST_swigregister = _e_cardlist.CARD_LIST_swigregister
CARD_LIST_swigregister(CARD_LIST)

# This file is compatible with both classic and new-style classes.

