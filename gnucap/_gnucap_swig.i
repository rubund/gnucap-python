// Copyright: 2009-2011 Henrik Johansson
// Author: Henrik Johansson

%module(directors="0", allprotected="1") gnucap_swig

// generate directors for all classes that have virtual methods
%feature(director);
%feature(nodirector) CARD;

%include stl.i
%include std_string.i
%include std_complex.i
%include c_comand.i
%include m_complex.i
%include std_shared_ptr.i

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
#include <memory>
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
typedef std::complex<double> COMPLEX;

%{

#include <md.h>

%}

struct COMPLEX_array_t {
  COMPLEX* _t;
};


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
//  void          fbsub(T* v) const;
  void          fbsub(T* x, const T* b, T* c = NULL) const;

  T     d(int r, int  )const    {return *(_diaptr[r]);}
 //  const T&    s(int r, int c);

private:
  T& m(int r, int c);
};


%template(BSMATRIXd) BSMATRIX<double>;
%template(BSMATRIXc) BSMATRIX<COMPLEX>;

%extend BSMATRIX<COMPLEX> {
  void fbsub_(COMPLEX_array_t& x){
    return self->fbsub(x._t);
  }
}



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

};

%extend CARD_LIST {
  CARD_LIST& card_list_(){
    return self->card_list;
  }
}

class SIM : public CMD {
protected:
  SIM();
public:
  ~SIM();
protected: // swig needs to know about these, apparently
  virtual void	setup(CS&)	= 0;
  virtual void	sweep()		= 0;
protected:
  virtual void	outdata(double, int);
  virtual void	head(double,double,const std::string&);
  virtual void	print_results(double);
  virtual void	alarm();
  virtual void	store_results(double);
protected:				/* s__solve.cc */
  void	advance_time();
};

// %typemap(in) SIM::TRACE(int x) {
//   $1 = SIM::TRACE(x);
// }

%extend SIM {
  inline SIM_DATA& sim_(){
    return *self->_sim;
  }
}


struct SIM_DATA{
  int _user_nodes;
  int _subckt_nodes;
  int _model_nodes;
  int _total_nodes;
  int _iter[iCOUNT];

  COMPLEX _jomega;	/* AC frequency to analyze at (radians) */
  bool _limiting;	/* flag: node limiting */
  double _vmax;
  double _vmin;
  bool _uic;		/* flag: use initial conditions (spice-like) */
  TRI_STATE _inc_mode;	/* flag: make incremental changes (3 state) */
  SIM_MODE _mode;	/* simulation type (AC, DC, ...) */
  SIM_PHASE _phase;	/* phase of simulation (iter, init-dc,) */
  int	*_nm;		/* node map (external to internal)	*/
  double *_i;		/* dc-tran current (i) vector		*/
  double *_v0;		/* dc-tran voltage, new			*/
  double *_vt1;		/* dc-tran voltage, 1 time ago		*/
			/*  used to restore after rejected step	*/
  COMPLEX_array_t _ac;		/* ac right side			*/
  LOGIC_NODE* _nstat;	/* digital data				*/
  double *_vdc;		/* saved dc voltages			*/
  BSMATRIX<double> _aa;	/* raw matrix for DC & tran */
  BSMATRIX<double> _lu;	/* decomposed matrix for DC & tran */
  BSMATRIX<COMPLEX> _acx;/* raw & decomposed matrix for AC */

  bool is_first_expand();
  void alloc_hold_vectors();
  void alloc_vectors();
  void unalloc_vectors();
  void uninit();
  void init();
  private:
  virtual void  setup(CS&)      = 0;
  virtual void  sweep()         = 0;
  virtual void  finish()        {}
  virtual bool  is_step_rejected()const {return false;}
public:
  void set_command_none() {_mode = s_NONE;}
  void set_command_ac()	  {_mode = s_AC;}
  void set_command_dc()	  {_mode = s_DC;}
  void set_command_op()	  {_mode = s_OP;}
  void set_command_tran() {_mode = s_TRAN;}
  void set_command_fourier() {_mode = s_FOURIER;}
  SIM_MODE sim_mode()	   {return _mode;}
  bool command_is_ac()	   {return _mode == s_AC;}
  bool command_is_dc()	   {return _mode == s_DC;}
  bool command_is_op()	   {return _mode == s_OP;}
  //bool command_is_tran()    {return _mode == s_TRAN;}
  //bool command_is_fourier() {return _mode == s_FOURIER;}
  bool analysis_is_ac()      {return _mode == s_AC;}
  bool analysis_is_dcop()    {return _mode == s_DC || _mode == s_OP;}
  bool analysis_is_static()  {return _phase == p_INIT_DC || _phase == p_DC_SWEEP;}
  bool analysis_is_restore() {return _phase == p_RESTORE;}
  bool analysis_is_tran()    {return _mode == s_TRAN || _mode == s_FOURIER;}
  bool analysis_is_tran_static()  {return analysis_is_tran() && _phase == p_INIT_DC;}
  bool analysis_is_tran_restore() {return analysis_is_tran() && _phase == p_RESTORE;}
  bool analysis_is_tran_dynamic() {return analysis_is_tran() && _phase == p_TRAN;}
};

// SIM_ is needed since Swig doesn't handle private virtual methods
// or protected enums.
// All non-status methods that are inherited from SIM should also be copied
// here or you will get segmentation faults (really?)
%inline %{
class SIM_ : public SIM {
protected:
  enum TRACE { // how much diagnostics to show
    tNONE      = 0,	/* no extended diagnostics			*/
    tUNDER     = 1,	/* show underlying analysis, important pts only	*/
    tALLTIME   = 2,	/* show every time step, including hidden 	*/
    tREJECTED  = 3,	/* show rejected time steps			*/
    tITERATION = 4,	/* show every iteration, including nonconverged	*/
    tVERBOSE   = 5	/* show extended diagnostics			*/
  };
protected:
  explicit SIM_() : SIM() { untested(); }
  ~SIM_() { untested(); }
public:
  virtual void  setup(CS&)=0;
  virtual void  sweep()=0;
  virtual void  do_it(CS&, CARD_LIST*){ incomplete(); };
public: // huh?
  virtual void	outdata(double d, int i){ return SIM::outdata(d, i);}
  virtual void	head(double a,double b, const std::string& s){
  return SIM::head(a,b,s);
  }
//  virtual void	print_results(double);
//  virtual void	alarm();
//  virtual void	store_results(double);
protected:
  bool solve(OPT::ITL a, unsigned b){
        return SIM::solve(a, SIM::TRACE(b));
  }
  bool solve_with_homotopy(OPT::ITL a, unsigned b){
        return SIM::solve_with_homotopy(a, SIM::TRACE(b));
  }
};
%}

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

STATUS status;

///////////////////////////////////////////////////////////////////////////////
// gnucap functions
///////////////////////////////////////////////////////////////////////////////
std::string command(char *command);
void parse(char *command);


// not needed: working around weird python memorymanagement?
// void uninstall_command(DISPATCHER<CMD>::INSTALL *installer);


//DISPATCHER<CMD>::INSTALL::~INSTALL();
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

#ifdef HAS_NUMPY
%init %{
      init_numpy();
%}
#endif




// vim:ts=8:sw=2:et:
