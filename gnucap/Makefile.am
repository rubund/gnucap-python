# gnucap-python python library Makefile.am
# Author: 2018 Felix Salfelder
# license GPLV3
#
# (inspired by now obsolete files from Henrik Johansson)
#
all-local:
	rm -f _gnucap.so
	${LN_S} .libs/_gnucap.so _gnucap.so

AM_CPPFLAGS=${CPPFLAGS} -I${top_srcdir}/include

dbg:
	print ${pythondir}

# python objects
# pythondir = bla
pythongcdir = $(pythondir)/gnucap
pythongc_PYTHON = gnucap.py __init__.py
pythongc_LTLIBRARIES = _gnucap.la
_gnucap_la_LDFLAGS = -module -omit-version
_gnucap_la_LIBADD = -lgnucap
_gnucap_la_SOURCES = command.cc numpy_interface.cc gnucap.i
# gen. (BUG)
_gnucap_la_SOURCES += c_genrat.cc
_gnucap_la_SOURCES += s_tr.cc s_tr_set.cc s_tr_swp.cc s__solve.cc s__out.cc s__init.cc
_gnucap_la_CPPFLAGS = @PYTHON_CPPFLAGS@ ${GC_CPPFLAGS} \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\" ${AM_CPPFLAGS}

%.py %.cxx %.h: %.i
	swig -python -c++ -Wall $(SWIG_FLAGS) -o WTF $<
	mv WTF gnucap.cxx
	mv WTF.h gnucap.h
	sed -i s/WTF/gnucap/ gnucap.cxx

.i.cxx:
.cxx.lo:

EXTRA_DIST = wrap.h

CLEANFILES = gnucap.h gnucap.py gnucap.cxx

