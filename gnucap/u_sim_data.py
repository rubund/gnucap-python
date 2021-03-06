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
        mname = '.'.join((pkg, '_u_sim_data')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_u_sim_data')
    _u_sim_data = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_u_sim_data', [dirname(__file__)])
        except ImportError:
            import _u_sim_data
            return _u_sim_data
        try:
            _mod = imp.load_module('_u_sim_data', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _u_sim_data = swig_import_helper()
    del swig_import_helper
else:
    import _u_sim_data
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


BUFLEN = _u_sim_data.BUFLEN
BIGBUFLEN = _u_sim_data.BIGBUFLEN
I_PROMPT = _u_sim_data.I_PROMPT
CKT_PROMPT = _u_sim_data.CKT_PROMPT
ANTI_COMMENT = _u_sim_data.ANTI_COMMENT
ENDDIR = _u_sim_data.ENDDIR
PATHSEP = _u_sim_data.PATHSEP
STEPFILE = _u_sim_data.STEPFILE
rPRE_MAIN = _u_sim_data.rPRE_MAIN
rPRESET = _u_sim_data.rPRESET
rINTERACTIVE = _u_sim_data.rINTERACTIVE
rSCRIPT = _u_sim_data.rSCRIPT
rBATCH = _u_sim_data.rBATCH
class ENV(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ENV, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ENV, name)
    __repr__ = _swig_repr
    __swig_setmethods__["run_mode"] = _u_sim_data.ENV_run_mode_set
    __swig_getmethods__["run_mode"] = _u_sim_data.ENV_run_mode_get
    if _newclass:
        run_mode = _swig_property(_u_sim_data.ENV_run_mode_get, _u_sim_data.ENV_run_mode_set)

    def __init__(self):
        this = _u_sim_data.new_ENV()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _u_sim_data.delete_ENV
    __del__ = lambda self: None
ENV_swigregister = _u_sim_data.ENV_swigregister
ENV_swigregister(ENV)
cvar = _u_sim_data.cvar

class COMPLEX_array_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, COMPLEX_array_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, COMPLEX_array_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_t"] = _u_sim_data.COMPLEX_array_t__t_set
    __swig_getmethods__["_t"] = _u_sim_data.COMPLEX_array_t__t_get
    if _newclass:
        _t = _swig_property(_u_sim_data.COMPLEX_array_t__t_get, _u_sim_data.COMPLEX_array_t__t_set)

    def __getitem__(self, i):
        return _u_sim_data.COMPLEX_array_t___getitem__(self, i)

    def __init__(self):
        this = _u_sim_data.new_COMPLEX_array_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _u_sim_data.delete_COMPLEX_array_t
    __del__ = lambda self: None
COMPLEX_array_t_swigregister = _u_sim_data.COMPLEX_array_t_swigregister
COMPLEX_array_t_swigregister(COMPLEX_array_t)

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _u_sim_data.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _u_sim_data.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _u_sim_data.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _u_sim_data.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _u_sim_data.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _u_sim_data.SwigPyIterator_equal(self, x)

    def copy(self):
        return _u_sim_data.SwigPyIterator_copy(self)

    def next(self):
        return _u_sim_data.SwigPyIterator_next(self)

    def __next__(self):
        return _u_sim_data.SwigPyIterator___next__(self)

    def previous(self):
        return _u_sim_data.SwigPyIterator_previous(self)

    def advance(self, n):
        return _u_sim_data.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _u_sim_data.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _u_sim_data.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _u_sim_data.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _u_sim_data.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _u_sim_data.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _u_sim_data.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _u_sim_data.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class BSMATRIXd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BSMATRIXd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BSMATRIXd, name)
    __repr__ = _swig_repr

    def __init__(self, ss=0):
        this = _u_sim_data.new_BSMATRIXd(ss)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def iwant(self, arg2, arg3):
        return _u_sim_data.BSMATRIXd_iwant(self, arg2, arg3)

    def unallocate(self):
        return _u_sim_data.BSMATRIXd_unallocate(self)

    def allocate(self):
        return _u_sim_data.BSMATRIXd_allocate(self)

    def reallocate(self):
        return _u_sim_data.BSMATRIXd_reallocate(self)

    def size(self):
        return _u_sim_data.BSMATRIXd_size(self)

    def density(self):
        return _u_sim_data.BSMATRIXd_density(self)

    def zero(self):
        return _u_sim_data.BSMATRIXd_zero(self)

    def dezero(self, o):
        return _u_sim_data.BSMATRIXd_dezero(self, o)

    def load_diagonal_point(self, i, value):
        return _u_sim_data.BSMATRIXd_load_diagonal_point(self, i, value)

    def load_point(self, i, j, value):
        return _u_sim_data.BSMATRIXd_load_point(self, i, j, value)

    def load_couple(self, i, j, value):
        return _u_sim_data.BSMATRIXd_load_couple(self, i, j, value)

    def load_symmetric(self, i, j, value):
        return _u_sim_data.BSMATRIXd_load_symmetric(self, i, j, value)

    def load_asymmetric(self, r1, r2, c1, c2, value):
        return _u_sim_data.BSMATRIXd_load_asymmetric(self, r1, r2, c1, c2, value)

    def lu_decomp(self, *args):
        return _u_sim_data.BSMATRIXd_lu_decomp(self, *args)

    def fbsub(self, x, b, c=None):
        return _u_sim_data.BSMATRIXd_fbsub(self, x, b, c)

    def d(self, r, arg3):
        return _u_sim_data.BSMATRIXd_d(self, r, arg3)
    __swig_destroy__ = _u_sim_data.delete_BSMATRIXd
    __del__ = lambda self: None
BSMATRIXd_swigregister = _u_sim_data.BSMATRIXd_swigregister
BSMATRIXd_swigregister(BSMATRIXd)

class BSMATRIXc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BSMATRIXc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BSMATRIXc, name)

    def __init__(self, ss=0):
        this = _u_sim_data.new_BSMATRIXc(ss)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def iwant(self, arg2, arg3):
        return _u_sim_data.BSMATRIXc_iwant(self, arg2, arg3)

    def unallocate(self):
        return _u_sim_data.BSMATRIXc_unallocate(self)

    def allocate(self):
        return _u_sim_data.BSMATRIXc_allocate(self)

    def reallocate(self):
        return _u_sim_data.BSMATRIXc_reallocate(self)

    def size(self):
        return _u_sim_data.BSMATRIXc_size(self)

    def density(self):
        return _u_sim_data.BSMATRIXc_density(self)

    def zero(self):
        return _u_sim_data.BSMATRIXc_zero(self)

    def dezero(self, o):
        return _u_sim_data.BSMATRIXc_dezero(self, o)

    def load_diagonal_point(self, i, value):
        return _u_sim_data.BSMATRIXc_load_diagonal_point(self, i, value)

    def load_point(self, i, j, value):
        return _u_sim_data.BSMATRIXc_load_point(self, i, j, value)

    def load_couple(self, i, j, value):
        return _u_sim_data.BSMATRIXc_load_couple(self, i, j, value)

    def load_symmetric(self, i, j, value):
        return _u_sim_data.BSMATRIXc_load_symmetric(self, i, j, value)

    def load_asymmetric(self, r1, r2, c1, c2, value):
        return _u_sim_data.BSMATRIXc_load_asymmetric(self, r1, r2, c1, c2, value)

    def lu_decomp(self, *args):
        return _u_sim_data.BSMATRIXc_lu_decomp(self, *args)

    def fbsub(self, x, b, c=None):
        return _u_sim_data.BSMATRIXc_fbsub(self, x, b, c)

    def d(self, r, arg3):
        return _u_sim_data.BSMATRIXc_d(self, r, arg3)

    def fbsub_(self, x):
        return _u_sim_data.BSMATRIXc_fbsub_(self, x)

    def __repr__(self):
        return _u_sim_data.BSMATRIXc___repr__(self)

    def __getitem__(self, p):
        return _u_sim_data.BSMATRIXc___getitem__(self, p)
    __swig_destroy__ = _u_sim_data.delete_BSMATRIXc
    __del__ = lambda self: None
BSMATRIXc_swigregister = _u_sim_data.BSMATRIXc_swigregister
BSMATRIXc_swigregister(BSMATRIXc)

class BSCR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BSCR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BSCR, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")

    def __repr__(self):
        return _u_sim_data.BSCR___repr__(self)

    def __getitem__(self, *args):
        return _u_sim_data.BSCR___getitem__(self, *args)
    __swig_destroy__ = _u_sim_data.delete_BSCR
    __del__ = lambda self: None
BSCR_swigregister = _u_sim_data.BSCR_swigregister
BSCR_swigregister(BSCR)

class SIM_DATA(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SIM_DATA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SIM_DATA, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_setmethods__["_user_nodes"] = _u_sim_data.SIM_DATA__user_nodes_set
    __swig_getmethods__["_user_nodes"] = _u_sim_data.SIM_DATA__user_nodes_get
    if _newclass:
        _user_nodes = _swig_property(_u_sim_data.SIM_DATA__user_nodes_get, _u_sim_data.SIM_DATA__user_nodes_set)
    __swig_setmethods__["_subckt_nodes"] = _u_sim_data.SIM_DATA__subckt_nodes_set
    __swig_getmethods__["_subckt_nodes"] = _u_sim_data.SIM_DATA__subckt_nodes_get
    if _newclass:
        _subckt_nodes = _swig_property(_u_sim_data.SIM_DATA__subckt_nodes_get, _u_sim_data.SIM_DATA__subckt_nodes_set)
    __swig_setmethods__["_model_nodes"] = _u_sim_data.SIM_DATA__model_nodes_set
    __swig_getmethods__["_model_nodes"] = _u_sim_data.SIM_DATA__model_nodes_get
    if _newclass:
        _model_nodes = _swig_property(_u_sim_data.SIM_DATA__model_nodes_get, _u_sim_data.SIM_DATA__model_nodes_set)
    __swig_setmethods__["_total_nodes"] = _u_sim_data.SIM_DATA__total_nodes_set
    __swig_getmethods__["_total_nodes"] = _u_sim_data.SIM_DATA__total_nodes_get
    if _newclass:
        _total_nodes = _swig_property(_u_sim_data.SIM_DATA__total_nodes_get, _u_sim_data.SIM_DATA__total_nodes_set)
    __swig_setmethods__["_iter"] = _u_sim_data.SIM_DATA__iter_set
    __swig_getmethods__["_iter"] = _u_sim_data.SIM_DATA__iter_get
    if _newclass:
        _iter = _swig_property(_u_sim_data.SIM_DATA__iter_get, _u_sim_data.SIM_DATA__iter_set)
    __swig_setmethods__["_jomega"] = _u_sim_data.SIM_DATA__jomega_set
    __swig_getmethods__["_jomega"] = _u_sim_data.SIM_DATA__jomega_get
    if _newclass:
        _jomega = _swig_property(_u_sim_data.SIM_DATA__jomega_get, _u_sim_data.SIM_DATA__jomega_set)
    __swig_setmethods__["_limiting"] = _u_sim_data.SIM_DATA__limiting_set
    __swig_getmethods__["_limiting"] = _u_sim_data.SIM_DATA__limiting_get
    if _newclass:
        _limiting = _swig_property(_u_sim_data.SIM_DATA__limiting_get, _u_sim_data.SIM_DATA__limiting_set)
    __swig_setmethods__["_vmax"] = _u_sim_data.SIM_DATA__vmax_set
    __swig_getmethods__["_vmax"] = _u_sim_data.SIM_DATA__vmax_get
    if _newclass:
        _vmax = _swig_property(_u_sim_data.SIM_DATA__vmax_get, _u_sim_data.SIM_DATA__vmax_set)
    __swig_setmethods__["_vmin"] = _u_sim_data.SIM_DATA__vmin_set
    __swig_getmethods__["_vmin"] = _u_sim_data.SIM_DATA__vmin_get
    if _newclass:
        _vmin = _swig_property(_u_sim_data.SIM_DATA__vmin_get, _u_sim_data.SIM_DATA__vmin_set)
    __swig_setmethods__["_uic"] = _u_sim_data.SIM_DATA__uic_set
    __swig_getmethods__["_uic"] = _u_sim_data.SIM_DATA__uic_get
    if _newclass:
        _uic = _swig_property(_u_sim_data.SIM_DATA__uic_get, _u_sim_data.SIM_DATA__uic_set)
    __swig_setmethods__["_inc_mode"] = _u_sim_data.SIM_DATA__inc_mode_set
    __swig_getmethods__["_inc_mode"] = _u_sim_data.SIM_DATA__inc_mode_get
    if _newclass:
        _inc_mode = _swig_property(_u_sim_data.SIM_DATA__inc_mode_get, _u_sim_data.SIM_DATA__inc_mode_set)
    __swig_setmethods__["_mode"] = _u_sim_data.SIM_DATA__mode_set
    __swig_getmethods__["_mode"] = _u_sim_data.SIM_DATA__mode_get
    if _newclass:
        _mode = _swig_property(_u_sim_data.SIM_DATA__mode_get, _u_sim_data.SIM_DATA__mode_set)
    __swig_setmethods__["_phase"] = _u_sim_data.SIM_DATA__phase_set
    __swig_getmethods__["_phase"] = _u_sim_data.SIM_DATA__phase_get
    if _newclass:
        _phase = _swig_property(_u_sim_data.SIM_DATA__phase_get, _u_sim_data.SIM_DATA__phase_set)
    __swig_setmethods__["_nm"] = _u_sim_data.SIM_DATA__nm_set
    __swig_getmethods__["_nm"] = _u_sim_data.SIM_DATA__nm_get
    if _newclass:
        _nm = _swig_property(_u_sim_data.SIM_DATA__nm_get, _u_sim_data.SIM_DATA__nm_set)
    __swig_setmethods__["_i"] = _u_sim_data.SIM_DATA__i_set
    __swig_getmethods__["_i"] = _u_sim_data.SIM_DATA__i_get
    if _newclass:
        _i = _swig_property(_u_sim_data.SIM_DATA__i_get, _u_sim_data.SIM_DATA__i_set)
    __swig_setmethods__["_v0"] = _u_sim_data.SIM_DATA__v0_set
    __swig_getmethods__["_v0"] = _u_sim_data.SIM_DATA__v0_get
    if _newclass:
        _v0 = _swig_property(_u_sim_data.SIM_DATA__v0_get, _u_sim_data.SIM_DATA__v0_set)
    __swig_setmethods__["_vt1"] = _u_sim_data.SIM_DATA__vt1_set
    __swig_getmethods__["_vt1"] = _u_sim_data.SIM_DATA__vt1_get
    if _newclass:
        _vt1 = _swig_property(_u_sim_data.SIM_DATA__vt1_get, _u_sim_data.SIM_DATA__vt1_set)
    __swig_setmethods__["_ac"] = _u_sim_data.SIM_DATA__ac_set
    __swig_getmethods__["_ac"] = _u_sim_data.SIM_DATA__ac_get
    if _newclass:
        _ac = _swig_property(_u_sim_data.SIM_DATA__ac_get, _u_sim_data.SIM_DATA__ac_set)
    __swig_setmethods__["_nstat"] = _u_sim_data.SIM_DATA__nstat_set
    __swig_getmethods__["_nstat"] = _u_sim_data.SIM_DATA__nstat_get
    if _newclass:
        _nstat = _swig_property(_u_sim_data.SIM_DATA__nstat_get, _u_sim_data.SIM_DATA__nstat_set)
    __swig_setmethods__["_vdc"] = _u_sim_data.SIM_DATA__vdc_set
    __swig_getmethods__["_vdc"] = _u_sim_data.SIM_DATA__vdc_get
    if _newclass:
        _vdc = _swig_property(_u_sim_data.SIM_DATA__vdc_get, _u_sim_data.SIM_DATA__vdc_set)
    __swig_setmethods__["_aa"] = _u_sim_data.SIM_DATA__aa_set
    __swig_getmethods__["_aa"] = _u_sim_data.SIM_DATA__aa_get
    if _newclass:
        _aa = _swig_property(_u_sim_data.SIM_DATA__aa_get, _u_sim_data.SIM_DATA__aa_set)
    __swig_setmethods__["_lu"] = _u_sim_data.SIM_DATA__lu_set
    __swig_getmethods__["_lu"] = _u_sim_data.SIM_DATA__lu_get
    if _newclass:
        _lu = _swig_property(_u_sim_data.SIM_DATA__lu_get, _u_sim_data.SIM_DATA__lu_set)
    __swig_setmethods__["_acx"] = _u_sim_data.SIM_DATA__acx_set
    __swig_getmethods__["_acx"] = _u_sim_data.SIM_DATA__acx_get
    if _newclass:
        _acx = _swig_property(_u_sim_data.SIM_DATA__acx_get, _u_sim_data.SIM_DATA__acx_set)

    def is_first_expand(self):
        return _u_sim_data.SIM_DATA_is_first_expand(self)

    def alloc_hold_vectors(self):
        return _u_sim_data.SIM_DATA_alloc_hold_vectors(self)

    def alloc_vectors(self):
        return _u_sim_data.SIM_DATA_alloc_vectors(self)

    def unalloc_vectors(self):
        return _u_sim_data.SIM_DATA_unalloc_vectors(self)

    def uninit(self):
        return _u_sim_data.SIM_DATA_uninit(self)

    def init(self):
        return _u_sim_data.SIM_DATA_init(self)

    def set_command_none(self):
        return _u_sim_data.SIM_DATA_set_command_none(self)

    def set_command_ac(self):
        return _u_sim_data.SIM_DATA_set_command_ac(self)

    def set_command_dc(self):
        return _u_sim_data.SIM_DATA_set_command_dc(self)

    def set_command_op(self):
        return _u_sim_data.SIM_DATA_set_command_op(self)

    def set_command_tran(self):
        return _u_sim_data.SIM_DATA_set_command_tran(self)

    def set_command_fourier(self):
        return _u_sim_data.SIM_DATA_set_command_fourier(self)

    def sim_mode(self):
        return _u_sim_data.SIM_DATA_sim_mode(self)

    def command_is_ac(self):
        return _u_sim_data.SIM_DATA_command_is_ac(self)

    def command_is_dc(self):
        return _u_sim_data.SIM_DATA_command_is_dc(self)

    def command_is_op(self):
        return _u_sim_data.SIM_DATA_command_is_op(self)

    def analysis_is_ac(self):
        return _u_sim_data.SIM_DATA_analysis_is_ac(self)

    def analysis_is_dcop(self):
        return _u_sim_data.SIM_DATA_analysis_is_dcop(self)

    def analysis_is_static(self):
        return _u_sim_data.SIM_DATA_analysis_is_static(self)

    def analysis_is_restore(self):
        return _u_sim_data.SIM_DATA_analysis_is_restore(self)

    def analysis_is_tran(self):
        return _u_sim_data.SIM_DATA_analysis_is_tran(self)

    def analysis_is_tran_static(self):
        return _u_sim_data.SIM_DATA_analysis_is_tran_static(self)

    def analysis_is_tran_restore(self):
        return _u_sim_data.SIM_DATA_analysis_is_tran_restore(self)

    def analysis_is_tran_dynamic(self):
        return _u_sim_data.SIM_DATA_analysis_is_tran_dynamic(self)
    __swig_destroy__ = _u_sim_data.delete_SIM_DATA
    __del__ = lambda self: None
SIM_DATA_swigregister = _u_sim_data.SIM_DATA_swigregister
SIM_DATA_swigregister(SIM_DATA)

# This file is compatible with both classic and new-style classes.


