#include <Python.h>
#include <string>

/*--------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/
int main()
{
  std::string file_name("comp.py");
  char *argv[] = {};
  FILE *fp;
  
  fp = fopen(file_name.c_str(), "r");
  
  if(fp == NULL) {
  }else{
  }
  

//  huh?! why not link?
  //  dlopen(PYTHON_SO, RTLD_NOW|RTLD_GLOBAL);
    Py_Initialize();
    PySys_SetArgv(0, argv);
    
    // Call init function of SWIG _gnucap module
 //   init_gnucap();

//    python_loaded = 1;

  PyRun_SimpleFile(fp, file_name.c_str());
}
