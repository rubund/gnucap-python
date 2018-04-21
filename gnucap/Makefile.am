# gnucap-python python library Makefile.am
# Author: 2018 Felix Salfelder
# license GPLV3
#
# (inspired by now obsolete files from Henrik Johansson)
#

AM_CPPFLAGS = \
	-I${top_srcdir}/include \
	@PYTHON_CPPFLAGS@ \
	${CPPFLAGS} \
	${GC_CPPFLAGS} \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\"

# python objects
pythongcdir = $(pythondir)/gnucap
pythongc_PYTHON = \
	${pythongc_LTLIBRARIES:_%.la=%.py} __init__.py

pythongc_LTLIBRARIES = \
	_gnucap_swig.la \
	_component.la \
	_globals.la \
	_m_cpoly.la \
	_m_wave.la \
	_c_exp.la \
	_e_elemnt.la \
	_e_node.la \
	_u_status.la

pkglib_LTLIBRARIES = libgnucap-python.la
libgnucap_python_la_SOURCES = garbage.cc


all-local:
	for i in ${pythongc_LTLIBRARIES:%.la=%.so}; do \
		rm -f $$i; \
		${LN_S} .libs/$$i $$i; \
	done

check: all-local

_gnucap_swig_la_LDFLAGS = -module -omit-version
AM_LDFLAGS = -module -omit-version

# AM_LIBADD?
_gnucap_swig_la_LIBADD = -lgnucap
_c_exp_la_LIBADD = -lgnucap
_component_la_LIBADD = -lgnucap
_globals_la_LIBADD = -lgnucap
_e_elemnt_la_LIBADD = -lgnucap
_e_node_la_LIBADD = -lgnucap
_m_cpoly_la_LIBADD = -lgnucap
_u_status_la_LIBADD = -lgnucap

_globals_la_LIBADD += libgnucap-python.la

AM_DEFAULT_SOURCE_EXT = .i

_gnucap_swig_la_SOURCES = command.cc numpy_interface.cc _gnucap_swig.i
_gnucap_swig_la_SOURCES += c_genrat.cc
_gnucap_swig_la_SOURCES += s_tr.cc s_tr_set.cc s_tr_swp.cc s__solve.cc s__out.cc s__init.cc

# why is this needed?
_gnucap_swig_la_CPPFLAGS = ${AM_CPPFLAGS}
_component_la_CPPFLAGS = ${AM_CPPFLAGS}
_globals_la_CPPFLAGS = ${AM_CPPFLAGS}
_c_exp_la_CPPFLAGS = ${AM_CPPFLAGS}
_e_elemnt_la_CPPFLAGS = ${AM_CPPFLAGS}
_m_wave_la_CPPFLAGS = ${AM_CPPFLAGS}
_m_cpoly_la_CPPFLAGS = ${AM_CPPFLAGS}
_e_node_la_CPPFLAGS = ${AM_CPPFLAGS}
_u_status_la_CPPFLAGS = ${AM_CPPFLAGS}

# (why) is this needed?
_component_la_SOURCES = _component.i

%.py _%.cxx _%.h: _%.i
	swig -python -c++ -Wall $(SWIG_FLAGS) -o _$*.cxx $<

.i.cxx:
.cxx.lo:

EXTRA_DIST = \
	wrap.h \
	e_card.i \
	e_base.i \
	c_comand.i \
	m_complex.i \
	_m_matrix.i

CLEANFILES = *~ *.pyc

CLEANFILES+= ${pythongc_LTLIBRARIES:_%.la=%.py}
CLEANFILES+= ${pythongc_LTLIBRARIES:%.la=%.cxx}
CLEANFILES+= ${pythongc_LTLIBRARIES:%.la=%.h}

#### dep
_e_elemnt.cxx: _e_node.i
_component.cxx: e_card.i e_base.i
_gnucap_swig.cxx: e_card.i e_base.i
