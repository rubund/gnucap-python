#include <u_lang.h>
#include <c_comand.h>
#include <globals.h>
#include <s__.h>

#include <Python.h>

// Swig _gnucap init function prototype
//extern "C" void init_gnucap();

/*--------------------------------------------------------------------------*/
namespace {
  static int python_loaded = 0;

/*--------------------------------------------------------------------------*/
void load_file(CS& cmd, OMSTREAM out, CARD_LIST* scope)
{ untested();
  std::string file_name;
  char *argv[] = {};
  FILE *fp;

  cmd >> file_name;
  
  fp = fopen(file_name.c_str(), "r");
  
  if(fp == NULL) {
    throw Exception_File_Open(std::string("Could not open ") + file_name);
  }else{
  }
  

//  huh?! why not link?
  if(!python_loaded) { untested();
	  trace0("dlopen python");
   // dlopen(PYTHON_SO, RTLD_NOW|RTLD_GLOBAL);
    Py_Initialize();
    PySys_SetArgv(0, argv);
    
    // Call init function of SWIG _gnucap module
 //   init_gnucap();

//    python_loaded = 1;
  }else{ untested();
  }

  trace1("running", file_name);
  PyRun_SimpleFile(fp, file_name.c_str());
}

/*--------------------------------------------------------------------------*/
class CMD_PYTHON : public CMD {
public:
  void do_it(CS& cmd, CARD_LIST* Scope)
  { untested();
    load_file(cmd, IO::mstdout, Scope);
  }
} p1;

DISPATCHER<CMD>::INSTALL d1(&command_dispatcher, "python", &p1);
/*--------------------------------------------------------------------------*/
}
