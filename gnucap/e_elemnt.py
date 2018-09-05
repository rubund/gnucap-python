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
        mname = '.'.join((pkg, '_e_elemnt')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_e_elemnt')
    _e_elemnt = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_e_elemnt', [dirname(__file__)])
        except ImportError:
            import _e_elemnt
            return _e_elemnt
        try:
            _mod = imp.load_module('_e_elemnt', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _e_elemnt = swig_import_helper()
    del swig_import_helper
else:
    import _e_elemnt
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
    __swig_destroy__ = _e_elemnt.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _e_elemnt.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _e_elemnt.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _e_elemnt.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _e_elemnt.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _e_elemnt.SwigPyIterator_equal(self, x)

    def copy(self):
        return _e_elemnt.SwigPyIterator_copy(self)

    def next(self):
        return _e_elemnt.SwigPyIterator_next(self)

    def __next__(self):
        return _e_elemnt.SwigPyIterator___next__(self)

    def previous(self):
        return _e_elemnt.SwigPyIterator_previous(self)

    def advance(self, n):
        return _e_elemnt.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _e_elemnt.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _e_elemnt.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _e_elemnt.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _e_elemnt.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _e_elemnt.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _e_elemnt.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _e_elemnt.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class PairDeque(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PairDeque, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PairDeque, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _e_elemnt.PairDeque_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _e_elemnt.PairDeque___nonzero__(self)

    def __bool__(self):
        return _e_elemnt.PairDeque___bool__(self)

    def __len__(self):
        return _e_elemnt.PairDeque___len__(self)

    def __getslice__(self, i, j):
        return _e_elemnt.PairDeque___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _e_elemnt.PairDeque___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _e_elemnt.PairDeque___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _e_elemnt.PairDeque___delitem__(self, *args)

    def __getitem__(self, *args):
        return _e_elemnt.PairDeque___getitem__(self, *args)

    def __setitem__(self, *args):
        return _e_elemnt.PairDeque___setitem__(self, *args)

    def pop(self):
        return _e_elemnt.PairDeque_pop(self)

    def append(self, x):
        return _e_elemnt.PairDeque_append(self, x)

    def empty(self):
        return _e_elemnt.PairDeque_empty(self)

    def size(self):
        return _e_elemnt.PairDeque_size(self)

    def swap(self, v):
        return _e_elemnt.PairDeque_swap(self, v)

    def begin(self):
        return _e_elemnt.PairDeque_begin(self)

    def end(self):
        return _e_elemnt.PairDeque_end(self)

    def rbegin(self):
        return _e_elemnt.PairDeque_rbegin(self)

    def rend(self):
        return _e_elemnt.PairDeque_rend(self)

    def clear(self):
        return _e_elemnt.PairDeque_clear(self)

    def get_allocator(self):
        return _e_elemnt.PairDeque_get_allocator(self)

    def pop_back(self):
        return _e_elemnt.PairDeque_pop_back(self)

    def erase(self, *args):
        return _e_elemnt.PairDeque_erase(self, *args)

    def __init__(self, *args):
        this = _e_elemnt.new_PairDeque(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _e_elemnt.PairDeque_push_back(self, x)

    def front(self):
        return _e_elemnt.PairDeque_front(self)

    def back(self):
        return _e_elemnt.PairDeque_back(self)

    def assign(self, n, x):
        return _e_elemnt.PairDeque_assign(self, n, x)

    def resize(self, *args):
        return _e_elemnt.PairDeque_resize(self, *args)

    def insert(self, *args):
        return _e_elemnt.PairDeque_insert(self, *args)

    def pop_front(self):
        return _e_elemnt.PairDeque_pop_front(self)

    def push_front(self, x):
        return _e_elemnt.PairDeque_push_front(self, x)
    __swig_destroy__ = _e_elemnt.delete_PairDeque
    __del__ = lambda self: None
PairDeque_swigregister = _e_elemnt.PairDeque_swigregister
PairDeque_swigregister(PairDeque)

class StopIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StopIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StopIterator, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _e_elemnt.new_StopIterator()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_StopIterator
    __del__ = lambda self: None
StopIterator_swigregister = _e_elemnt.StopIterator_swigregister
StopIterator_swigregister(StopIterator)

class WaveIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WaveIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WaveIterator, name)
    __repr__ = _swig_repr

    def __init__(self, _cur, _end):
        this = _e_elemnt.new_WaveIterator(_cur, _end)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iter__(self):
        return _e_elemnt.WaveIterator___iter__(self)
    __swig_setmethods__["cur"] = _e_elemnt.WaveIterator_cur_set
    __swig_getmethods__["cur"] = _e_elemnt.WaveIterator_cur_get
    if _newclass:
        cur = _swig_property(_e_elemnt.WaveIterator_cur_get, _e_elemnt.WaveIterator_cur_set)
    __swig_setmethods__["end"] = _e_elemnt.WaveIterator_end_set
    __swig_getmethods__["end"] = _e_elemnt.WaveIterator_end_get
    if _newclass:
        end = _swig_property(_e_elemnt.WaveIterator_end_get, _e_elemnt.WaveIterator_end_set)

    def __next__(self):
        return _e_elemnt.WaveIterator___next__(self)

    def next(self):
        return _e_elemnt.WaveIterator_next(self)
    __swig_destroy__ = _e_elemnt.delete_WaveIterator
    __del__ = lambda self: None
WaveIterator_swigregister = _e_elemnt.WaveIterator_swigregister
WaveIterator_swigregister(WaveIterator)

class WAVE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WAVE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WAVE, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _e_elemnt.new_WAVE(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_WAVE
    __del__ = lambda self: None

    def set_delay(self, d):
        return _e_elemnt.WAVE_set_delay(self, d)

    def initialize(self):
        return _e_elemnt.WAVE_initialize(self)

    def push(self, t, v):
        return _e_elemnt.WAVE_push(self, t, v)

    def v_out(self, t):
        return _e_elemnt.WAVE_v_out(self, t)

    def v_reflect(self, t, v_total):
        return _e_elemnt.WAVE_v_reflect(self, t, v_total)

    def __iadd__(self, *args):
        return _e_elemnt.WAVE___iadd__(self, *args)

    def __imul__(self, *args):
        return _e_elemnt.WAVE___imul__(self, *args)

    def begin(self):
        return _e_elemnt.WAVE_begin(self)

    def end(self):
        return _e_elemnt.WAVE_end(self)

    def __iter__(self):
        return _e_elemnt.WAVE___iter__(self)
WAVE_swigregister = _e_elemnt.WAVE_swigregister
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
        find_wave = staticmethod(_e_elemnt.CKT_BASE_find_wave)
    else:
        find_wave = _e_elemnt.CKT_BASE_find_wave
CKT_BASE_swigregister = _e_elemnt.CKT_BASE_swigregister
CKT_BASE_swigregister(CKT_BASE)

def CKT_BASE_find_wave(arg2):
    return _e_elemnt.CKT_BASE_find_wave(arg2)
CKT_BASE_find_wave = _e_elemnt.CKT_BASE_find_wave

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
    __swig_destroy__ = _e_elemnt.delete_CARD
    __del__ = lambda self: None

    def value_name(self):
        return _e_elemnt.CARD_value_name(self)

    def param_is_printable(self, arg2):
        return _e_elemnt.CARD_param_is_printable(self, arg2)

    def param_name(self, *args):
        return _e_elemnt.CARD_param_name(self, *args)

    def param_value(self, arg2):
        return _e_elemnt.CARD_param_value(self, arg2)

    def set_param_by_name(self, arg2, arg3):
        return _e_elemnt.CARD_set_param_by_name(self, arg2, arg3)

    def set_param_by_index(self, arg2, arg3, arg4):
        return _e_elemnt.CARD_set_param_by_index(self, arg2, arg3, arg4)

    def param_count(self):
        return _e_elemnt.CARD_param_count(self)
CARD_swigregister = _e_elemnt.CARD_swigregister
CARD_swigregister(CARD)

SHARED_PTR_DISOWN = _e_elemnt.SHARED_PTR_DISOWN

# this will end up somewhere in component.py

class COMPONENT_(CARD):
    __swig_setmethods__ = {}
    for _s in [CARD]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, COMPONENT_, name, value)
    __swig_getmethods__ = {}
    for _s in [CARD]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, COMPONENT_, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        if self.__class__ == COMPONENT_:
            _self = None
        else:
            _self = self
        this = _e_elemnt.new_COMPONENT_(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_COMPONENT_
    __del__ = lambda self: None

    def port_name(self, arg0):
        return _e_elemnt.COMPONENT__port_name(self, arg0)

    def port_value(self, i):
        return _e_elemnt.COMPONENT__port_value(self, i)

    def param_count(self):
        return _e_elemnt.COMPONENT__param_count(self)

    def param_is_printable(self, arg0):
        return _e_elemnt.COMPONENT__param_is_printable(self, arg0)

    def tr_probe_num(self, arg0):
        return _e_elemnt.COMPONENT__tr_probe_num(self, arg0)

    def value_name(self):
        return _e_elemnt.COMPONENT__value_name(self)

    def clone(self):
        return _e_elemnt.COMPONENT__clone(self)

    def dev_type(self):
        return _e_elemnt.COMPONENT__dev_type(self)

    def long_label(self):
        return _e_elemnt.COMPONENT__long_label(self)

    def max_nodes(self):
        return _e_elemnt.COMPONENT__max_nodes(self)

    def min_nodes(self):
        return _e_elemnt.COMPONENT__min_nodes(self)

    def net_nodes(self):
        return _e_elemnt.COMPONENT__net_nodes(self)

    def num_current_ports(self):
        return _e_elemnt.COMPONENT__num_current_ports(self)

    def tail_size(self):
        return _e_elemnt.COMPONENT__tail_size(self)
    __swig_setmethods__["_n"] = _e_elemnt.COMPONENT___n_set
    __swig_getmethods__["_n"] = _e_elemnt.COMPONENT___n_get
    if _newclass:
        _n = _swig_property(_e_elemnt.COMPONENT___n_get, _e_elemnt.COMPONENT___n_set)
    def __disown__(self):
        self.this.disown()
        _e_elemnt.disown_COMPONENT_(self)
        return weakref_proxy(self)
COMPONENT__swigregister = _e_elemnt.COMPONENT__swigregister
COMPONENT__swigregister(COMPONENT_)

class node_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, node_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, node_t, name)
    __repr__ = _swig_repr

    def m_(self):
        return _e_elemnt.node_t_m_(self)

    def t_(self):
        return _e_elemnt.node_t_t_(self)

    def e_(self):
        return _e_elemnt.node_t_e_(self)

    def short_label(self):
        return _e_elemnt.node_t_short_label(self)

    def set_to_ground(self, arg2):
        return _e_elemnt.node_t_set_to_ground(self, arg2)

    def new_node(self, arg2, arg3):
        return _e_elemnt.node_t_new_node(self, arg2, arg3)

    def new_model_node(self, n, d):
        return _e_elemnt.node_t_new_model_node(self, n, d)

    def map_subckt_node(self, map_array, d):
        return _e_elemnt.node_t_map_subckt_node(self, map_array, d)

    def is_grounded(self):
        return _e_elemnt.node_t_is_grounded(self)

    def is_connected(self):
        return _e_elemnt.node_t_is_connected(self)

    def __init__(self, *args):
        this = _e_elemnt.new_node_t(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_node_t
    __del__ = lambda self: None

    def __deref__(self):
        return _e_elemnt.node_t___deref__(self)

    def __eq__(self, p):
        return _e_elemnt.node_t___eq__(self, p)

    def v0(self):
        return _e_elemnt.node_t_v0(self)

    def vac(self):
        return _e_elemnt.node_t_vac(self)

    def i(self):
        return _e_elemnt.node_t_i(self)
node_t_swigregister = _e_elemnt.node_t_swigregister
node_t_swigregister(node_t)

class nodearray_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nodearray_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nodearray_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_t"] = _e_elemnt.nodearray_t__t_set
    __swig_getmethods__["_t"] = _e_elemnt.nodearray_t__t_get
    if _newclass:
        _t = _swig_property(_e_elemnt.nodearray_t__t_get, _e_elemnt.nodearray_t__t_set)

    def __getitem__(self, i):
        return _e_elemnt.nodearray_t___getitem__(self, i)

    def __init__(self):
        this = _e_elemnt.new_nodearray_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_nodearray_t
    __del__ = lambda self: None
nodearray_t_swigregister = _e_elemnt.nodearray_t_swigregister
nodearray_t_swigregister(nodearray_t)


def get_node(n, x):
    return _e_elemnt.get_node(n, x)
get_node = _e_elemnt.get_node
class FPOLY1(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FPOLY1, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FPOLY1, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _e_elemnt.FPOLY1_x_set
    __swig_getmethods__["x"] = _e_elemnt.FPOLY1_x_get
    if _newclass:
        x = _swig_property(_e_elemnt.FPOLY1_x_get, _e_elemnt.FPOLY1_x_set)
    __swig_setmethods__["f0"] = _e_elemnt.FPOLY1_f0_set
    __swig_getmethods__["f0"] = _e_elemnt.FPOLY1_f0_get
    if _newclass:
        f0 = _swig_property(_e_elemnt.FPOLY1_f0_get, _e_elemnt.FPOLY1_f0_set)
    __swig_setmethods__["f1"] = _e_elemnt.FPOLY1_f1_set
    __swig_getmethods__["f1"] = _e_elemnt.FPOLY1_f1_get
    if _newclass:
        f1 = _swig_property(_e_elemnt.FPOLY1_f1_get, _e_elemnt.FPOLY1_f1_set)

    def __init__(self, *args):
        this = _e_elemnt.new_FPOLY1(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_FPOLY1
    __del__ = lambda self: None

    def __eq__(self, p):
        return _e_elemnt.FPOLY1___eq__(self, p)

    def __imul__(self, *args):
        return _e_elemnt.FPOLY1___imul__(self, *args)

    def __iadd__(self, *args):
        return _e_elemnt.FPOLY1___iadd__(self, *args)

    def __neg__(self):
        return _e_elemnt.FPOLY1___neg__(self)

    def c1(self):
        return _e_elemnt.FPOLY1_c1(self)

    def c0(self):
        return _e_elemnt.FPOLY1_c0(self)
FPOLY1_swigregister = _e_elemnt.FPOLY1_swigregister
FPOLY1_swigregister(FPOLY1)

class CPOLY1(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPOLY1, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPOLY1, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _e_elemnt.CPOLY1_x_set
    __swig_getmethods__["x"] = _e_elemnt.CPOLY1_x_get
    if _newclass:
        x = _swig_property(_e_elemnt.CPOLY1_x_get, _e_elemnt.CPOLY1_x_set)
    __swig_setmethods__["c0"] = _e_elemnt.CPOLY1_c0_set
    __swig_getmethods__["c0"] = _e_elemnt.CPOLY1_c0_get
    if _newclass:
        c0 = _swig_property(_e_elemnt.CPOLY1_c0_get, _e_elemnt.CPOLY1_c0_set)
    __swig_setmethods__["c1"] = _e_elemnt.CPOLY1_c1_set
    __swig_getmethods__["c1"] = _e_elemnt.CPOLY1_c1_get
    if _newclass:
        c1 = _swig_property(_e_elemnt.CPOLY1_c1_get, _e_elemnt.CPOLY1_c1_set)

    def __init__(self, *args):
        this = _e_elemnt.new_CPOLY1(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _e_elemnt.delete_CPOLY1
    __del__ = lambda self: None

    def __eq__(self, p):
        return _e_elemnt.CPOLY1___eq__(self, p)

    def __imul__(self, s):
        return _e_elemnt.CPOLY1___imul__(self, s)

    def f1(self):
        return _e_elemnt.CPOLY1_f1(self)

    def f0(self):
        return _e_elemnt.CPOLY1_f0(self)
CPOLY1_swigregister = _e_elemnt.CPOLY1_swigregister
CPOLY1_swigregister(CPOLY1)

class ELEMENT(CARD):
    __swig_setmethods__ = {}
    for _s in [CARD]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ELEMENT, name, value)
    __swig_getmethods__ = {}
    for _s in [CARD]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ELEMENT, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        if self.__class__ == ELEMENT:
            _self = None
        else:
            _self = self
        this = _e_elemnt.new_ELEMENT(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def store_values(self):
        return _e_elemnt.ELEMENT_store_values(self)

    def clone(self):
        return _e_elemnt.ELEMENT_clone(self)

    def port_name(self, arg0):
        return _e_elemnt.ELEMENT_port_name(self, arg0)

    def dev_type(self):
        return _e_elemnt.ELEMENT_dev_type(self)

    def max_nodes(self):
        return _e_elemnt.ELEMENT_max_nodes(self)

    def min_nodes(self):
        return _e_elemnt.ELEMENT_min_nodes(self)

    def net_nodes(self):
        return _e_elemnt.ELEMENT_net_nodes(self)

    def matrix_nodes(self):
        return _e_elemnt.ELEMENT_matrix_nodes(self)

    def num_current_ports(self):
        return _e_elemnt.ELEMENT_num_current_ports(self)

    def tail_size(self):
        return _e_elemnt.ELEMENT_tail_size(self)

    def precalc_last(self):
        return _e_elemnt.ELEMENT_precalc_last(self)

    def tr_begin(self):
        return _e_elemnt.ELEMENT_tr_begin(self)

    def tr_load(self):
        return _e_elemnt.ELEMENT_tr_load(self)

    def tr_unload(self):
        return _e_elemnt.ELEMENT_tr_unload(self)

    def set_constant(self, c):
        return _e_elemnt.ELEMENT_set_constant(self, c)

    def skip_dev_type(self, arg2):
        return _e_elemnt.ELEMENT_skip_dev_type(self, arg2)

    def print_type_in_spice(self):
        return _e_elemnt.ELEMENT_print_type_in_spice(self)

    def tr_restore(self):
        return _e_elemnt.ELEMENT_tr_restore(self)

    def dc_advance(self):
        return _e_elemnt.ELEMENT_dc_advance(self)

    def tr_advance(self):
        return _e_elemnt.ELEMENT_tr_advance(self)

    def tr_regress(self):
        return _e_elemnt.ELEMENT_tr_regress(self)

    def tr_needs_eval(self):
        return _e_elemnt.ELEMENT_tr_needs_eval(self)

    def tr_review(self):
        return _e_elemnt.ELEMENT_tr_review(self)

    def long_label(self):
        return _e_elemnt.ELEMENT_long_label(self)

    def tr_iwant_matrix(self):
        return _e_elemnt.ELEMENT_tr_iwant_matrix(self)

    def ac_iwant_matrix(self):
        return _e_elemnt.ELEMENT_ac_iwant_matrix(self)

    def dampdiff(self, arg2, arg3):
        return _e_elemnt.ELEMENT_dampdiff(self, arg2, arg3)

    def tr_load_inode(self):
        return _e_elemnt.ELEMENT_tr_load_inode(self)

    def tr_unload_inode(self):
        return _e_elemnt.ELEMENT_tr_unload_inode(self)

    def ac_load_inode(self):
        return _e_elemnt.ELEMENT_ac_load_inode(self)

    def tr_load_shunt(self):
        return _e_elemnt.ELEMENT_tr_load_shunt(self)

    def tr_unload_shunt(self):
        return _e_elemnt.ELEMENT_tr_unload_shunt(self)

    def ac_load_shunt(self):
        return _e_elemnt.ELEMENT_ac_load_shunt(self)

    def tr_load_source(self):
        return _e_elemnt.ELEMENT_tr_load_source(self)

    def tr_unload_source(self):
        return _e_elemnt.ELEMENT_tr_unload_source(self)

    def ac_load_source(self):
        return _e_elemnt.ELEMENT_ac_load_source(self)

    def tr_load_couple(self):
        return _e_elemnt.ELEMENT_tr_load_couple(self)

    def tr_unload_couple(self):
        return _e_elemnt.ELEMENT_tr_unload_couple(self)

    def ac_load_couple(self):
        return _e_elemnt.ELEMENT_ac_load_couple(self)

    def tr_load_passive(self):
        return _e_elemnt.ELEMENT_tr_load_passive(self)

    def tr_unload_passive(self):
        return _e_elemnt.ELEMENT_tr_unload_passive(self)

    def ac_load_passive(self):
        return _e_elemnt.ELEMENT_ac_load_passive(self)

    def tr_load_active(self):
        return _e_elemnt.ELEMENT_tr_load_active(self)

    def tr_unload_active(self):
        return _e_elemnt.ELEMENT_tr_unload_active(self)

    def ac_load_active(self):
        return _e_elemnt.ELEMENT_ac_load_active(self)

    def tr_load_extended(self, no1, no2, ni1, ni2, value, old_value):
        return _e_elemnt.ELEMENT_tr_load_extended(self, no1, no2, ni1, ni2, value, old_value)

    def ac_load_extended(self, no1, no2, ni1, ni2, value):
        return _e_elemnt.ELEMENT_ac_load_extended(self, no1, no2, ni1, ni2, value)

    def tr_load_source_point(self, no1, value, old_value):
        return _e_elemnt.ELEMENT_tr_load_source_point(self, no1, value, old_value)

    def ac_load_source_point(self, no1, new_value):
        return _e_elemnt.ELEMENT_ac_load_source_point(self, no1, new_value)

    def tr_load_diagonal_point(self, no1, value, old_value):
        return _e_elemnt.ELEMENT_tr_load_diagonal_point(self, no1, value, old_value)

    def ac_load_diagonal_point(self, no1, value):
        return _e_elemnt.ELEMENT_ac_load_diagonal_point(self, no1, value)

    def tr_load_point(self, no1, no2, value, old_value):
        return _e_elemnt.ELEMENT_tr_load_point(self, no1, no2, value, old_value)

    def ac_load_point(self, no1, no2, value):
        return _e_elemnt.ELEMENT_ac_load_point(self, no1, no2, value)

    def conv_check(self):
        return _e_elemnt.ELEMENT_conv_check(self)

    def has_tr_eval(self):
        return _e_elemnt.ELEMENT_has_tr_eval(self)

    def has_ac_eval(self):
        return _e_elemnt.ELEMENT_has_ac_eval(self)

    def using_tr_eval(self):
        return _e_elemnt.ELEMENT_using_tr_eval(self)

    def using_ac_eval(self):
        return _e_elemnt.ELEMENT_using_ac_eval(self)

    def tr_eval(self):
        return _e_elemnt.ELEMENT_tr_eval(self)

    def ac_eval(self):
        return _e_elemnt.ELEMENT_ac_eval(self)

    def tr_iwant_matrix_passive(self):
        return _e_elemnt.ELEMENT_tr_iwant_matrix_passive(self)

    def tr_iwant_matrix_active(self):
        return _e_elemnt.ELEMENT_tr_iwant_matrix_active(self)

    def tr_iwant_matrix_extended(self):
        return _e_elemnt.ELEMENT_tr_iwant_matrix_extended(self)

    def ac_iwant_matrix_passive(self):
        return _e_elemnt.ELEMENT_ac_iwant_matrix_passive(self)

    def ac_iwant_matrix_active(self):
        return _e_elemnt.ELEMENT_ac_iwant_matrix_active(self)

    def ac_iwant_matrix_extended(self):
        return _e_elemnt.ELEMENT_ac_iwant_matrix_extended(self)

    def tr_review_trunc_error(self, q):
        return _e_elemnt.ELEMENT_tr_review_trunc_error(self, q)

    def tr_review_check_and_convert(self, timestep):
        return _e_elemnt.ELEMENT_tr_review_check_and_convert(self, timestep)

    def tr_outvolts(self):
        return _e_elemnt.ELEMENT_tr_outvolts(self)

    def tr_outvolts_limited(self):
        return _e_elemnt.ELEMENT_tr_outvolts_limited(self)

    def ac_outvolts(self):
        return _e_elemnt.ELEMENT_ac_outvolts(self)

    def tr_involts(self):
        return _e_elemnt.ELEMENT_tr_involts(self)

    def tr_input(self):
        return _e_elemnt.ELEMENT_tr_input(self)

    def tr_involts_limited(self):
        return _e_elemnt.ELEMENT_tr_involts_limited(self)

    def tr_input_limited(self):
        return _e_elemnt.ELEMENT_tr_input_limited(self)

    def tr_amps(self):
        return _e_elemnt.ELEMENT_tr_amps(self)

    def ac_involts(self):
        return _e_elemnt.ELEMENT_ac_involts(self)

    def ac_amps(self):
        return _e_elemnt.ELEMENT_ac_amps(self)

    def order(self):
        return _e_elemnt.ELEMENT_order(self)

    def error_factor(self):
        return _e_elemnt.ELEMENT_error_factor(self)

    def param_count(self):
        return _e_elemnt.ELEMENT_param_count(self)

    def param_is_printable(self, arg0):
        return _e_elemnt.ELEMENT_param_is_printable(self, arg0)

    def tr_probe_num(self, arg0):
        return _e_elemnt.ELEMENT_tr_probe_num(self, arg0)

    def value_name(self):
        return _e_elemnt.ELEMENT_value_name(self)
    __swig_setmethods__["_loaditer"] = _e_elemnt.ELEMENT__loaditer_set
    __swig_getmethods__["_loaditer"] = _e_elemnt.ELEMENT__loaditer_get
    if _newclass:
        _loaditer = _swig_property(_e_elemnt.ELEMENT__loaditer_get, _e_elemnt.ELEMENT__loaditer_set)
    __swig_setmethods__["_n"] = _e_elemnt.ELEMENT__n_set
    __swig_getmethods__["_n"] = _e_elemnt.ELEMENT__n_get
    if _newclass:
        _n = _swig_property(_e_elemnt.ELEMENT__n_get, _e_elemnt.ELEMENT__n_set)
    __swig_setmethods__["_m0"] = _e_elemnt.ELEMENT__m0_set
    __swig_getmethods__["_m0"] = _e_elemnt.ELEMENT__m0_get
    if _newclass:
        _m0 = _swig_property(_e_elemnt.ELEMENT__m0_get, _e_elemnt.ELEMENT__m0_set)
    __swig_setmethods__["_m1"] = _e_elemnt.ELEMENT__m1_set
    __swig_getmethods__["_m1"] = _e_elemnt.ELEMENT__m1_get
    if _newclass:
        _m1 = _swig_property(_e_elemnt.ELEMENT__m1_get, _e_elemnt.ELEMENT__m1_set)
    __swig_setmethods__["_loss0"] = _e_elemnt.ELEMENT__loss0_set
    __swig_getmethods__["_loss0"] = _e_elemnt.ELEMENT__loss0_get
    if _newclass:
        _loss0 = _swig_property(_e_elemnt.ELEMENT__loss0_get, _e_elemnt.ELEMENT__loss0_set)
    __swig_setmethods__["_loss1"] = _e_elemnt.ELEMENT__loss1_set
    __swig_getmethods__["_loss1"] = _e_elemnt.ELEMENT__loss1_get
    if _newclass:
        _loss1 = _swig_property(_e_elemnt.ELEMENT__loss1_get, _e_elemnt.ELEMENT__loss1_set)
    __swig_setmethods__["_acg"] = _e_elemnt.ELEMENT__acg_set
    __swig_getmethods__["_acg"] = _e_elemnt.ELEMENT__acg_get
    if _newclass:
        _acg = _swig_property(_e_elemnt.ELEMENT__acg_get, _e_elemnt.ELEMENT__acg_set)
    __swig_setmethods__["_ev"] = _e_elemnt.ELEMENT__ev_set
    __swig_getmethods__["_ev"] = _e_elemnt.ELEMENT__ev_get
    if _newclass:
        _ev = _swig_property(_e_elemnt.ELEMENT__ev_get, _e_elemnt.ELEMENT__ev_set)
    __swig_setmethods__["_dt"] = _e_elemnt.ELEMENT__dt_set
    __swig_getmethods__["_dt"] = _e_elemnt.ELEMENT__dt_get
    if _newclass:
        _dt = _swig_property(_e_elemnt.ELEMENT__dt_get, _e_elemnt.ELEMENT__dt_set)
    __swig_setmethods__["_time"] = _e_elemnt.ELEMENT__time_set
    __swig_getmethods__["_time"] = _e_elemnt.ELEMENT__time_get
    if _newclass:
        _time = _swig_property(_e_elemnt.ELEMENT__time_get, _e_elemnt.ELEMENT__time_set)
    __swig_setmethods__["_y1"] = _e_elemnt.ELEMENT__y1_set
    __swig_getmethods__["_y1"] = _e_elemnt.ELEMENT__y1_get
    if _newclass:
        _y1 = _swig_property(_e_elemnt.ELEMENT__y1_get, _e_elemnt.ELEMENT__y1_set)

    def _y_(self, i):
        return _e_elemnt.ELEMENT__y_(self, i)

    def element_tr_begin(self):
        return _e_elemnt.ELEMENT_element_tr_begin(self)

    def element_precalc_last(self):
        return _e_elemnt.ELEMENT_element_precalc_last(self)
    def __disown__(self):
        self.this.disown()
        _e_elemnt.disown_ELEMENT(self)
        return weakref_proxy(self)
ELEMENT_swigregister = _e_elemnt.ELEMENT_swigregister
ELEMENT_swigregister(ELEMENT)

# This file is compatible with both classic and new-style classes.


