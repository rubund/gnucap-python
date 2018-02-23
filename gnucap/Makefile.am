# gnucap-python python library Makefile.am
# Author: 2018 Felix Salfelder
# license GPLV3
#
# (inspired by now obsolete files from Henrik Johansson)
#
all-local:
	rm -f _gnucap_swig.so
	${LN_S} .libs/_gnucap_swig.so _gnucap_swig.so

AM_CPPFLAGS=${CPPFLAGS} -I${top_srcdir}/include

dbg:
	print ${pythondir}

# python objects
# pythondir = bla
pythongcdir = $(pythondir)/gnucap
pythongc_PYTHON = gnucap_swig.py __init__.py
pythongc_LTLIBRARIES = _gnucap_swig.la
_gnucap_swig_la_LDFLAGS = -module -omit-version
_gnucap_swig_la_LIBADD = -lgnucap
_gnucap_swig_la_SOURCES = command.cc numpy_interface.cc gnucap_swig.i
# gen. (BUG)
_gnucap_swig_la_SOURCES += c_genrat.cc
_gnucap_swig_la_SOURCES += s_tr.cc s_tr_set.cc s_tr_swp.cc s__solve.cc s__out.cc s__init.cc
_gnucap_swig_la_CPPFLAGS = \
	@PYTHON_CPPFLAGS@ \
	${AM_CPPFLAGS} \
	${GC_CPPFLAGS} \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\"

%.py %.cxx %.h: %.i
	swig -python -c++ -Wall $(SWIG_FLAGS) -o $*.cxx $<

.i.cxx:
.cxx.lo:

EXTRA_DIST = wrap.h

CLEANFILES = gnucap_swig.h gnucap_swig.py gnucap_swig.cxx

