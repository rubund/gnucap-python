%module(directors="0", allprotected="1") component

// generate directors for all classes that have virtual methods
%feature("director");
// %feature("nodirector") TRANSIENT; 
%feature(nodirector) CARD;
%feature("nodirector") COMPONENT;

%include stl.i
%include std_string.i
%include std_complex.i
%include e_card.i

%{
#include "wrap.h"
#include <e_compon.h>
#include <globals.h>
%}


%exception {
    try {
        $action
    } catch (Exception& e) {
      PyErr_SetString(PyExc_Exception, e.message().c_str());
      return NULL;
    }
}
%allowexception;

class COMPONENT : public CARD {
protected:
  COMPONENT();
  ~COMPONENT() { unreachable(); }
public:

protected: // swig needs to know about these, apparently
  virtual void	clone(CS&) = 0;
};

class component : public COMPONENT {
protected:
  component();
  virtual ~component();
public: // why? (what does the implementation do?)
  virtual CARD*	 clone()const{ unreachable(); }
  virtual std::string port_name(int)const { untested(); return "INCOMPLETE"; }
  virtual std::string value_name()const { untested();   return "INCOMPLETE"; }
};

%pythoncode %{
# WHAT IS THIS?
%}


class card_install{
public:
  card_install(DISPATCHER<CARD>* d, const std::string& name, CARD* p);
};

// THIS IS DEPRECATED. possibly there's a good way now?!
// (its working)
%nestedworkaround DISPATCHER<CARD>::INSTALL;

DISPATCHER<CARD> device_dispatcher;

%{
typedef DISPATCHER<CARD>::INSTALL card_install;
%}

card_install install_device(char *name, CARD *c);

// vim:ts=8:sw=2:et:
