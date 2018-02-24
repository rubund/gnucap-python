%module(directors="0", allprotected="1") gnucap_swig

// generate directors for all classes that have virtual methods
%feature("director");
// %feature("nodirector") TRANSIENT; 
// %feature(nodirector) CMD;
// %feature(nodirector) SIM;

%include stl.i
%include std_string.i
%include std_complex.i

%{
#include "wrap.h"
#include <ap.h>
#include <c_comand.h>
#include <l_dispatcher.h>
#include <s__.h>
#include <m_wave.h>
#include <u_opt.h>
#include <e_cardlist.h>
#include <globals.h>
#include <md.h>
#include <m_matrix.h>
#include <u_status.h>
#include <s_tr.h>
#include <u_time_pair.h>
#include <u_sim_data.h>
#include <globals.h>
%}

#ifdef HAS_NUMPY
%{
#include "numpy_interface.h"
%}
#endif

%exception {
    try {
        $action
    } catch (Exception& e) {
      PyErr_SetString(PyExc_Exception, e.message().c_str());
      return NULL;
    }
}
%allowexception;

///////////////////////////////////////////////////////////////////////////////
// Basic types
///////////////////////////////////////////////////////////////////////////////
//%template(COMPLEX) std::complex<double>;

///////////////////////////////////////////////////////////////////////////////
// BSMATRIX
///////////////////////////////////////////////////////////////////////////////
template<class T> class BSMATRIX {
public:
  BSMATRIX(int ss=0);

  void          iwant(int, int);
  void          unallocate();
  void          allocate();
  void          reallocate();
  int           size()const;
  double        density();
  void          zero();
  void          dezero(T& o);
  void          load_diagonal_point(int i, T value);
  void          load_point(int i, int j, T value);
  void          load_couple(int i, int j, T value);
  void          load_symmetric(int i, int j, T value);
  void          load_asymmetric(int r1, int r2, int c1, int c2, T value);

  void          lu_decomp(const BSMATRIX<T>&, bool do_partial);
  void          lu_decomp();
  void          fbsub(T* v) const;
  void          fbsub(T* x, const T* b, T* c = NULL) const;

  T     d(int r, int  )const    {return *(_diaptr[r]);}
 //  const T&    s(int r, int c);

private:
  T& m(int r, int c);
};

%template(BSMATRIXd) BSMATRIX<double>;
%template(BSMATRIXc) BSMATRIX<COMPLEX>;


///////////////////////////////////////////////////////////////////////////////
// Major gnucap classes
///////////////////////////////////////////////////////////////////////////////

class CS {
public:
      enum STRING {_STRING};
      CS(CS::STRING, const std::string& s);
      const std::string fullstring()const;
};

class CARD_LIST {
public:
   CARD_LIST& expand();
   CARD_LIST& map_nodes();
   CARD_LIST& tr_iwant_matrix();
   CARD_LIST& tr_begin();
   CARD_LIST& tr_restore();
   CARD_LIST& dc_advance();
   CARD_LIST& tr_advance();
   CARD_LIST& tr_regress();
   bool       tr_needs_eval()const;
   CARD_LIST& tr_queue_eval();
   bool       do_tr();
   CARD_LIST& tr_load();
   TIME_PAIR  tr_review();
   CARD_LIST& tr_accept();
   CARD_LIST& tr_unload();
   CARD_LIST& ac_iwant_matrix();
   CARD_LIST& ac_begin();
   CARD_LIST& do_ac();
   CARD_LIST& ac_load();

   static CARD_LIST card_list; // in globals.cc
};

class CKT_BASE {
protected:
  explicit CKT_BASE()                     :_probes(0), _label() {}
  explicit CKT_BASE(const std::string& s) :_probes(0), _label(s) {}
  explicit CKT_BASE(const CKT_BASE& p)    :_probes(0), _label(p._label) {}
  virtual  ~CKT_BASE();
public:
  static WAVE* find_wave(const std::string&);

  virtual bool help(CS&, OMSTREAM&) const{ untested(); }

};

class CMD : public CKT_BASE {
public:
  std::string value_name()const {return "";}
  virtual void do_it(CS&, CARD_LIST*) = 0;
  virtual ~CMD() {}
  static  void  cmdproc(CS&, CARD_LIST*);
  static  void	command(const std::string&, CARD_LIST*);
};

class SIM : public CMD {
protected:
  SIM();
public:
  ~SIM();

protected: // swig needs to know about these, apparently
  virtual void	setup(CS&)	= 0;
  virtual void	sweep()		= 0;
};

struct SIM_DATA{
  int _user_nodes;
  int _subckt_nodes;
  int _model_nodes;
  int _total_nodes;
  int _iter[iCOUNT];


  void init();
  void uninit();
  private:
  virtual void  setup(CS&)      = 0;
  virtual void  sweep()         = 0;
  virtual void  finish()        {}
  virtual bool  is_step_rejected()const {return false;}
};

// The sim is needed since Swig doesn't handle private virtual methods
// All non-status methods that are inherited from SIM should also be copied
// here or you will get segmentation faults
class sim : public SIM {
protected:
  explicit sim():SIM()  { untested(); }
  ~sim() { untested(); }
public:
  virtual void  setup(CS&)      = 0;
  virtual void  sweep()         = 0;
  void  do_it(CS&, CARD_LIST*)       {incomplete();}
protected:
  const PROBELIST& alarmlist()const;     /* s__out.cc */
  const PROBELIST& plotlist()const;
  const PROBELIST& printlist()const;
  const PROBELIST& storelist()const;
  void   outdata(double, int);
  void   head(double,double,const std::string&);
  void   print_results(double);
  void   alarm();
  virtual void  store_results(double);
private:
  const std::string long_label()const {unreachable(); return "";}
protected: // what's this?
//         void   alloc_vectors();
//  static void   unalloc_vectors(); 
};

class TRANSIENT : public SIM {
public:
        void do_it(CS&, CARD_LIST* scope);
        TRANSIENT();
        ~TRANSIENT();
        virtual void accept();
private:
        void  setup(CS&);
protected:
        bool _cont;
        void sweep();
        void outdata(double, int);
};

class STATUS {
public:
//  void command(CS& cmd);

  int control;
  int hidden_steps;
};

enum RUN_MODE {
  rPRE_MAIN,    /* it hasn't got to main yet                    */
  rPRESET,      /* do set up commands now, but not simulation   */
                /* store parameters, so bare invocation of a    */
                /* simulation command will do it this way.      */
  rINTERACTIVE, /* run the commands, interactively              */
  rSCRIPT,      /* execute now, as a command, then restore mode */
  rBATCH        /* execute now, as a command, then exit         */
};

class SET_RUN_MODE {
public:
      SET_RUN_MODE(RUN_MODE rm);
};
// ENV::run_mode;

class ENV {
public:
  static RUN_MODE run_mode; // variations on handling of dot commands
};

///////////////////////////////////////////////////////////////////////////////
// Global variables
///////////////////////////////////////////////////////////////////////////////
//RUN_MODE ENV::run_mode = rPRE_MAIN;
//DISPATCHER<CMD> command_dispatcher;
//DISPATCHER<COMMON_COMPONENT> bm_dispatcher;
//DISPATCHER<MODEL_CARD> model_dispatcher;
//DISPATCHER<CARD> device_dispatcher;
//DISPATCHER<LANGUAGE> language_dispatcher;
//DISPATCHER<FUNCTION> function_dispatcher;
STATUS status;

///////////////////////////////////////////////////////////////////////////////
// gnucap functions
///////////////////////////////////////////////////////////////////////////////
std::string command(char *command);
void parse(char *command);
void uninstall_command(DISPATCHER<CMD>::INSTALL *installer);

class cmd_install{
public:
  cmd_install(DISPATCHER<CMD>* d, const std::string& name, CMD* p);
};

// THIS IS DEPRECATED. possibly there's a good way now?!
// (it works)
%nestedworkaround DISPATCHER<CMD>::INSTALL;


%{
typedef DISPATCHER<CMD>::INSTALL cmd_install;
%}

cmd_install install_command(char *command_name, CMD *cmd);

DISPATCHER<CMD>::INSTALL::~INSTALL();
///////////////////////////////////////////////////////////////////////////////
// non-gnucap utility functions
///////////////////////////////////////////////////////////////////////////////
#ifdef HAS_NUMPY
void init_numpy();
PyObject *wave_to_arrays(WAVE *wave);
PyObject *bsmatrix_to_array_d(BSMATRIX<double> &A);
PyObject *bsmatrix_to_array_c(BSMATRIX<COMPLEX> &A);
PyObject *to_double_array(double *data, int len);
PyObject *get_complex_array(COMPLEX *data, int len);
void set_complex_array(COMPLEX *data, PyObject *srcarray);

template<class T> void bsmatrix_fbsub_array(BSMATRIX<T> *A, PyObject *rhs, PyObject *dest);

%template(bsmatrix_fbsub_array_double) bsmatrix_fbsub_array<double>;

#endif

///////////////////////////////////////////////////////////////////////////////
// init
///////////////////////////////////////////////////////////////////////////////
#ifdef HAS_NUMPY
%init %{
      init_numpy();
%}
#endif

///////////////////////////////////////////////////////////////////////////////
// python code
///////////////////////////////////////////////////////////////////////////////
%pythoncode %{
%}

// vim:ts=8:sw=2:et:
