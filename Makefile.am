## $Id$
##
## Top level automake file for gnucap

# this is a hack
all-local:
	ln -sf .libs/python.so _gnucap.so


pluginsdir = $(libdir)/gnucap

AM_CPPFLAGS=${GC_CPPFLAGS}

plugins_LTLIBRARIES = python.la

python_la_SOURCES = c_python.cc gnucap.cc gnucap_wrap.cxx

# yikes. the python stuff should use the dispatcher to get hold of s__*
# (these are verbatim copies of the upstream apps)
python_la_SOURCES += s_tr.cc s_tr_set.cc s_tr_swp.cc s__solve.cc s__out.cc s__init.cc

# gen. (BUG)
python_la_SOURCES += c_genrat.cc


if NUMPY
  python_la_SOURCES += numpy_interface.cc
  SWIG_FLAGS = -DHAS_NUMPY
endif

python_la_CPPFLAGS = @PYTHON_CPPFLAGS@ \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\" ${AM_CPPFLAGS}

python_la_CFLAGS = -fPIC ${DEPS_CFLAGS}

python_la_LDFLAGS = -shared -module -avoid-version @LDFLAGS@ @PYTHON_LDFLAGS@

python_la_LIBADD = ${DEPS_LIBS} @PYTHON_EXTRA_LIBS@ @GC_LIBS@

ACLOCAL_AMFLAGS = -I m4

# ouch. also builds .h?
%_wrap.cxx: %.i
	swig -python -c++ -Wall $(SWIG_FLAGS) $<

CLEANFILES = gnucap_wrap.cxx gnucap_wrap.h gnucap.py
