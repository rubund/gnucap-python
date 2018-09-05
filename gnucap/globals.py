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
        mname = '.'.join((pkg, '_globals')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_globals')
    _globals = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_globals', [dirname(__file__)])
        except ImportError:
            import _globals
            return _globals
        try:
            _mod = imp.load_module('_globals', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _globals = swig_import_helper()
    del swig_import_helper
else:
    import _globals
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


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _globals.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _globals.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _globals.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _globals.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _globals.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _globals.SwigPyIterator_equal(self, x)

    def copy(self):
        return _globals.SwigPyIterator_copy(self)

    def next(self):
        return _globals.SwigPyIterator_next(self)

    def __next__(self):
        return _globals.SwigPyIterator___next__(self)

    def previous(self):
        return _globals.SwigPyIterator_previous(self)

    def advance(self, n):
        return _globals.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _globals.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _globals.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _globals.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _globals.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _globals.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _globals.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _globals.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class PairDeque(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PairDeque, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PairDeque, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _globals.PairDeque_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _globals.PairDeque___nonzero__(self)

    def __bool__(self):
        return _globals.PairDeque___bool__(self)

    def __len__(self):
        return _globals.PairDeque___len__(self)

    def __getslice__(self, i, j):
        return _globals.PairDeque___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _globals.PairDeque___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _globals.PairDeque___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _globals.PairDeque___delitem__(self, *args)

    def __getitem__(self, *args):
        return _globals.PairDeque___getitem__(self, *args)

    def __setitem__(self, *args):
        return _globals.PairDeque___setitem__(self, *args)

    def pop(self):
        return _globals.PairDeque_pop(self)

    def append(self, x):
        return _globals.PairDeque_append(self, x)

    def empty(self):
        return _globals.PairDeque_empty(self)

    def size(self):
        return _globals.PairDeque_size(self)

    def swap(self, v):
        return _globals.PairDeque_swap(self, v)

    def begin(self):
        return _globals.PairDeque_begin(self)

    def end(self):
        return _globals.PairDeque_end(self)

    def rbegin(self):
        return _globals.PairDeque_rbegin(self)

    def rend(self):
        return _globals.PairDeque_rend(self)

    def clear(self):
        return _globals.PairDeque_clear(self)

    def get_allocator(self):
        return _globals.PairDeque_get_allocator(self)

    def pop_back(self):
        return _globals.PairDeque_pop_back(self)

    def erase(self, *args):
        return _globals.PairDeque_erase(self, *args)

    def __init__(self, *args):
        this = _globals.new_PairDeque(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _globals.PairDeque_push_back(self, x)

    def front(self):
        return _globals.PairDeque_front(self)

    def back(self):
        return _globals.PairDeque_back(self)

    def assign(self, n, x):
        return _globals.PairDeque_assign(self, n, x)

    def resize(self, *args):
        return _globals.PairDeque_resize(self, *args)

    def insert(self, *args):
        return _globals.PairDeque_insert(self, *args)

    def pop_front(self):
        return _globals.PairDeque_pop_front(self)

    def push_front(self, x):
        return _globals.PairDeque_push_front(self, x)
    __swig_destroy__ = _globals.delete_PairDeque
    __del__ = lambda self: None
PairDeque_swigregister = _globals.PairDeque_swigregister
PairDeque_swigregister(PairDeque)

class StopIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StopIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StopIterator, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _globals.new_StopIterator()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _globals.delete_StopIterator
    __del__ = lambda self: None
StopIterator_swigregister = _globals.StopIterator_swigregister
StopIterator_swigregister(StopIterator)

class WaveIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WaveIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WaveIterator, name)
    __repr__ = _swig_repr

    def __init__(self, _cur, _end):
        this = _globals.new_WaveIterator(_cur, _end)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iter__(self):
        return _globals.WaveIterator___iter__(self)
    __swig_setmethods__["cur"] = _globals.WaveIterator_cur_set
    __swig_getmethods__["cur"] = _globals.WaveIterator_cur_get
    if _newclass:
        cur = _swig_property(_globals.WaveIterator_cur_get, _globals.WaveIterator_cur_set)
    __swig_setmethods__["end"] = _globals.WaveIterator_end_set
    __swig_getmethods__["end"] = _globals.WaveIterator_end_get
    if _newclass:
        end = _swig_property(_globals.WaveIterator_end_get, _globals.WaveIterator_end_set)

    def __next__(self):
        return _globals.WaveIterator___next__(self)

    def next(self):
        return _globals.WaveIterator_next(self)
    __swig_destroy__ = _globals.delete_WaveIterator
    __del__ = lambda self: None
WaveIterator_swigregister = _globals.WaveIterator_swigregister
WaveIterator_swigregister(WaveIterator)

class WAVE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WAVE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WAVE, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _globals.new_WAVE(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _globals.delete_WAVE
    __del__ = lambda self: None

    def set_delay(self, d):
        return _globals.WAVE_set_delay(self, d)

    def initialize(self):
        return _globals.WAVE_initialize(self)

    def push(self, t, v):
        return _globals.WAVE_push(self, t, v)

    def v_out(self, t):
        return _globals.WAVE_v_out(self, t)

    def v_reflect(self, t, v_total):
        return _globals.WAVE_v_reflect(self, t, v_total)

    def __iadd__(self, *args):
        return _globals.WAVE___iadd__(self, *args)

    def __imul__(self, *args):
        return _globals.WAVE___imul__(self, *args)

    def begin(self):
        return _globals.WAVE_begin(self)

    def end(self):
        return _globals.WAVE_end(self)

    def __iter__(self):
        return _globals.WAVE___iter__(self)
WAVE_swigregister = _globals.WAVE_swigregister
WAVE_swigregister(WAVE)

class CKT_BASE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CKT_BASE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CKT_BASE, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        find_wave = staticmethod(_globals.CKT_BASE_find_wave)
    else:
        find_wave = _globals.CKT_BASE_find_wave
CKT_BASE_swigregister = _globals.CKT_BASE_swigregister
CKT_BASE_swigregister(CKT_BASE)

def CKT_BASE_find_wave(arg2):
    return _globals.CKT_BASE_find_wave(arg2)
CKT_BASE_find_wave = _globals.CKT_BASE_find_wave

class CARD(CKT_BASE):
    __swig_setmethods__ = {}
    for _s in [CKT_BASE]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CARD, name, value)
    __swig_getmethods__ = {}
    for _s in [CKT_BASE]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CARD, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _globals.delete_CARD
    __del__ = lambda self: None

    def value_name(self):
        return _globals.CARD_value_name(self)

    def param_is_printable(self, arg2):
        return _globals.CARD_param_is_printable(self, arg2)

    def param_name(self, *args):
        return _globals.CARD_param_name(self, *args)

    def param_value(self, arg2):
        return _globals.CARD_param_value(self, arg2)

    def set_param_by_name(self, arg2, arg3):
        return _globals.CARD_set_param_by_name(self, arg2, arg3)

    def set_param_by_index(self, arg2, arg3, arg4):
        return _globals.CARD_set_param_by_index(self, arg2, arg3, arg4)

    def param_count(self):
        return _globals.CARD_param_count(self)
CARD_swigregister = _globals.CARD_swigregister
CARD_swigregister(CARD)

SHARED_PTR_DISOWN = _globals.SHARED_PTR_DISOWN

def install_device(name, card):
    return _globals.install_device(name, card)
install_device = _globals.install_device

def install_command(name, cmd):
    return _globals.install_command(name, cmd)
install_command = _globals.install_command
class shared_card_installer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shared_card_installer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shared_card_installer, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _globals.delete_shared_card_installer
    __del__ = lambda self: None

    def __init__(self):
        this = _globals.new_shared_card_installer()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
shared_card_installer_swigregister = _globals.shared_card_installer_swigregister
shared_card_installer_swigregister(shared_card_installer)

class shared_command_installer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shared_command_installer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shared_command_installer, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _globals.delete_shared_command_installer
    __del__ = lambda self: None

    def __init__(self):
        this = _globals.new_shared_command_installer()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
shared_command_installer_swigregister = _globals.shared_command_installer_swigregister
shared_command_installer_swigregister(shared_command_installer)


def need_default_plugins():
    return _globals.need_default_plugins()
need_default_plugins = _globals.need_default_plugins
# This file is compatible with both classic and new-style classes.


