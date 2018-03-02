# gnucap-python top level Makefile.am
# Author: 2018 Felix Salfelder
# license GPLV3
#
# (inspired by now obsolete files from Henrik Johansson)
#
check_PROGRAMS = test_python
test_python_SOURCES = test_python.cc

test_python_LDADD = ${DEPS_LIBS} @PYTHON_EXTRA_LIBS@ -lpython2.7


test_python_CPPFLAGS = ${GC_CPPFLAGS} @PYTHON_CPPFLAGS@ \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\" ${AM_CPPFLAGS}

ACLOCAL_AMFLAGS = -I m4
SUBDIRS = include gnucap

all-local:
	rm -f c_python.so
	${LN_S} .libs/c_python.so c_python.so


# gnucap plugins
pluginsdir = $(libdir)/gnucap
plugins_LTLIBRARIES = c_python.la

c_python_la_SOURCES = c_python.cc # gnucap_wrap.cxx
c_python_la_CXXFLAGS = -Wall ${AM_CXXFLAGS} -fPIC ${DEPS_CFLAGS}

# BUG: it does not work without NUMPY either.
if NUMPY
  c_python_la_SOURCES += # numpy_interface.cc
  SWIG_FLAGS = -DHAS_NUMPY
endif

c_python_la_CPPFLAGS = ${GC_CPPFLAGS} @PYTHON_CPPFLAGS@ \
	-DPYTHON_SO=\"@ac_python_libdir@/@ac_python_soname@\" ${AM_CPPFLAGS}

c_python_la_LDFLAGS = -shared -module -avoid-version @LDFLAGS@ @PYTHON_LDFLAGS@
c_python_la_LIBADD = ${DEPS_LIBS} @PYTHON_EXTRA_LIBS@

# possibly required on non-posix systems
#c_python_la_LIBADD += @GC_LIBS@

####### TESTS #########

M_TESTS_ENVIRONMENT = \
    export REDIRECT='exec 2>&9'\
           MAKEFLAGS=--no-print-directory \
           srcdir='$(srcdir)';
AM_TESTS_FD_REDIRECT = 9>&2
TEST_EXTENSIONS = .gc .py
PY_LOG_COMPILER = $(top_srcdir)/py_log_compiler

PY_TESTS = \
	elmt.py \
	sim.py \
	comp.py

# not yet.
# PY_TESTS += store.py

TESTS = ${PY_TESTS}

${PY_TESTS:%.py=%.py.out}: %.py.out: %.py
	python < ${srcdir}/$*.py > $@

.PHONY: .P
.P:
	@:

$(PY_TESTS:%.py=%.py.out): .P
$(PY_TESTS:%.gc=%.log): .P

EXTRA_DIST=py_log_compiler ${TESTS} ${TESTS:%=%.ref}
