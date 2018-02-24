#include <c_comand.h>
#include <l_dispatcher.h>
#include <s__.h>
#include <memory>

#if 0
class sim : public SIM {
protected:
  explicit sim() : SIM() { untested(); }
  ~sim() { untested(); }
public:
  virtual void  setup(CS&)=0;
  virtual void  sweep()=0;
  virtual void  do_it(CS&, CARD_LIST*){ incomplete(); };
};
#endif

#include <e_compon.h>

#if 0
class component : public COMPONENT {
protected:
  explicit component(const COMPONENT& c) : COMPONENT(c) { untested(); }
  explicit component() : COMPONENT() { untested(); }

public: // these pure in COMPONENT
  virtual CARD*	 clone()const{ unreachable(); }
  virtual std::string port_name(int)const { unreachable(); }
  virtual std::string value_name()const { unreachable(); }

public:	// obsolete -- do not use in new code
  bool print_type_in_spice()const { untested(); return false; }
  bool use_obsolete_callback_parse()const { untested(); return false; }
  bool use_obsolete_callback_print()const { untested(); return false; }
  void print_args_obsolete_callback(OMSTREAM&, LANGUAGE*)const { unreachable(); }
  void obsolete_move_parameters_from_common(const COMMON_COMPONENT*) { unreachable(); }
};
#endif

class card : public CARD {
public:
  explicit card() : CARD()  {}
public: // pure?
  virtual CARD* clone(CS&){ unreachable(); }
};

std::string command(char *command);
void parse(char *command);


//DISPATCHER<CARD>::INSTALL install_device(char *name, CARD*);

inline void test_dummy(CARD *c){ untested(); }

#if 0
namespace{
struct test{
	class ct: public component {
	};
	test(){
		ct x;
		CARD* y = &x;
	}
};
}
#endif


// maybe later
void uninstall_command(DISPATCHER<CMD>::INSTALL *installer);
