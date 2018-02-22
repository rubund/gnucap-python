%module(directors="0", allprotected="1") gnucap

// generate directors for all classes that have virtual methods
%feature("director");
%feature("nodirector") TRANSIENT; 
%feature(nodirector) CMD;
%feature(nodirector) SIM;

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

#if 0
class CARD : public CKT_BASE {
protected:                              // create and destroy.
private:
  CARD();
  CARD(const CARD&);
public:
  virtual  ~CARD()                      {delete _subckt;}

public: // parameters
  virtual std::string value_name()const = 0;

  virtual bool param_is_printable(int)const;
  virtual std::string param_name(int)const;
  virtual std::string param_name(int,int)const;
  virtual std::string param_value(int)const;
  virtual void set_param_by_name(std::string, std::string);
  virtual void set_param_by_index(int, std::string&, int);
  virtual int param_count()const {return 0;}
};
#endif
class CARD : public CKT_BASE {
private:
  mutable int	_evaliter;	// model eval iteration number
  CARD_LIST*	_subckt;
  CARD* 	_owner;
  bool		_constant;	// eval stays the same every iteration
protected:
  node_t*	_n;
public:
  int		_net_nodes;	// actual number of "nodes" in the netlist
  //--------------------------------------------------------------------
public:   				// traversal functions
  CARD* find_in_my_scope(const std::string& name);
  const CARD* find_in_my_scope(const std::string& name)const;
  const CARD* find_in_parent_scope(const std::string& name)const;
  const CARD* find_looking_out(const std::string& name)const;
  //--------------------------------------------------------------------
protected: // create and destroy.
  explicit CARD();
  explicit CARD(const CARD&);
public:
  virtual  ~CARD();
  virtual CARD*	 clone()const = 0;
  virtual CARD*	 clone_instance()const  {return clone();}
  //--------------------------------------------------------------------
public:	// "elaborate"
  virtual void	 precalc_first()	{}
  virtual void	 expand_first()		{}
  virtual void	 expand()		{}
  virtual void	 expand_last()		{}
  virtual void	 precalc_last()		{}
  virtual void	 map_nodes()		{}
  //--------------------------------------------------------------------
public:	// dc-tran
  virtual void	 tr_iwant_matrix()	{}
  virtual void	 tr_begin()		{}
  virtual void	 tr_restore()		{}
  virtual void	 dc_advance()		{}
  virtual void	 tr_advance()		{}
  virtual void	 tr_regress()		{}
  virtual bool	 tr_needs_eval()const	{return false;}
  virtual void	 tr_queue_eval()	{}
  virtual bool	 do_tr()		{return true;}
  virtual bool	 do_tr_last()		{return true;}
  virtual void	 tr_load()		{}
  virtual TIME_PAIR tr_review();	//{return TIME_PAIR(NEVER,NEVER);}
  virtual void	 tr_accept()		{}
  virtual void	 tr_unload()		{untested();}
  //--------------------------------------------------------------------
public:	// ac
  virtual void	 ac_iwant_matrix()	{}
  virtual void	 ac_begin()		{}
  virtual void	 do_ac()		{}
  virtual void	 ac_load()		{}
  //--------------------------------------------------------------------
public:	// state, aux data
  virtual char id_letter()const	{unreachable(); return '\0';}
  virtual int  net_nodes()const	{untested();return 0;}
  virtual bool is_device()const	{return false;}
  virtual void set_slave()	{untested(); assert(!subckt());}
	  bool evaluated()const;

  void	set_constant(bool c)	{_constant = c;}
  bool	is_constant()const	{return _constant;}
  //--------------------------------------------------------------------
public: // owner, scope
  virtual CARD_LIST*	   scope();
  virtual const CARD_LIST* scope()const;
  virtual bool		   makes_own_scope()const  {return false;}

  CARD*		owner()		   {return _owner;}
  const CARD*	owner()const	   {return _owner;}
  void		set_owner(CARD* o) {assert(!_owner||_owner==o); _owner=o;}
  //--------------------------------------------------------------------
public: // subckt
  CARD_LIST*	     subckt()		{return _subckt;}
  const CARD_LIST*   subckt()const	{return _subckt;}
  void	  new_subckt();
  void	  new_subckt(const CARD* model, PARAM_LIST* p);
  void	  renew_subckt(const CARD* model, PARAM_LIST* p);
  //void     new_subckt(const CARD* model, CARD* owner, const CARD_LIST* scope, PARAM_LIST* p);
  //void     renew_subckt(const CARD* model, CARD* owner, const CARD_LIST* scope, PARAM_LIST* p);
  //--------------------------------------------------------------------
public:	// type
  virtual std::string dev_type()const	{unreachable(); return "";}
  virtual void set_dev_type(const std::string&);
  //--------------------------------------------------------------------
public:	// label -- in CKT_BASE
  // non-virtual void set_label(const std::string& s) //BASE
  // non-virtual const std::string& short_label()const //BASE
  /*virtual*/ const std::string long_label()const; // no further override
  //--------------------------------------------------------------------
public:	// ports -- mostly defer to COMPONENT
  node_t& n_(int i)const;
  int     connects_to(const node_t& node)const;
  //--------------------------------------------------------------------
public: // parameters
  virtual void set_param_by_name(std::string, std::string);
  virtual void set_param_by_index(int i, std::string&, int offset)
				{untested(); throw Exception_Too_Many(i, 0, offset);}
  virtual int  param_count_dont_print()const	   {return 0;}
  virtual int  param_count()const		   {return 0;}
  virtual bool param_is_printable(int)const	   {untested(); return false;}
  virtual std::string param_name(int)const	   {return "";}
  virtual std::string param_name(int i,int j)const {return (j==0) ? param_name(i) : "";}
  virtual std::string param_value(int)const	   {untested(); return "";}
  virtual std::string value_name()const = 0;
  //--------------------------------------------------------------------
public:	// obsolete -- do not use in new code
  virtual bool use_obsolete_callback_parse()const {return false;}
  virtual bool use_obsolete_callback_print()const {return false;}
  virtual void print_args_obsolete_callback(OMSTREAM&,LANGUAGE*)const {unreachable();}
};

#if 0
class CMD : public CARD { 
public:            
      CMD();
      virtual ~CMD();
      virtual void do_it(CS& cmd, CARD_LIST*)=0;
      std::string value_name()const;
      static void command(const std::string&, CARD_LIST*);
      static void cmdproc(CS&, CARD_LIST*);
  // virtual CARD*	 clone()const { incomplete();}
};
#endif

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

// The SIMWrapper is needed since Swig doesn't handle private virtual methods
// All non-status methods that are inherited from SIM should also be copied 
// here or you will get segmentation faults
class SIMWrapper : public SIM {
public:
  explicit SIMWrapper():SIM()  {}
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
DISPATCHER<CMD>::INSTALL *attach_command(char *command_name, CMD *cmd);
void detach_command(DISPATCHER<CMD>::INSTALL *installer);

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
