# gnucap-python top level Makefile.am
# Author: 2018 Felix Salfelder
# license GPLV3
#
# (inspired by now obsolete files from Henrik Johansson)

ACLOCAL_AMFLAGS = -I m4
SUBDIRS = include gnucap

all-local:
	rm -f _gnucap.so
	${LN_S} .libs/_gnucap.so _gnucap.so
	rm -f python.so
	${LN_S} .libs/python.so python.so


# gnucap plugins
pluginsdir = $(libdir)/gnucap
plugins_LTLIBRARIES = python.la

python_la_SOURCES = c_python.cc # gnucap_wrap.cxx
python_la_CXXFLAGS = -Wall ${AM_CXXFLAGS} -fPIC ${DEPS_CFLAGS}

# BUG: it does not work without NUMPY either.
if NUMPY
  python_la_SOURCES += # numpy_interface.cc
  SWIG_FLAGS = -DHAS_NUMPY
endif

python_la_CPPFLAGS = ${GC_CPPFLAGS} @PYTHON_CPPFLAGS@ \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\" ${AM_CPPFLAGS}

python_la_LDFLAGS = -shared -module -avoid-version @LDFLAGS@ @PYTHON_LDFLAGS@
python_la_LIBADD = ${DEPS_LIBS} @PYTHON_EXTRA_LIBS@ @GC_LIBS@
