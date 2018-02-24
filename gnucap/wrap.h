#include <c_comand.h>
#include <l_dispatcher.h>
#include <s__.h>

class sim : public SIM {
protected:
  explicit sim() : SIM() { untested(); }
  ~sim() { untested(); }
public:
  virtual void  setup(CS&)=0;
  virtual void  sweep()=0;
  virtual void  do_it(CS&, CARD_LIST*){ incomplete(); };
};

#include <e_compon.h>
class component : public COMPONENT {
public:
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

class card : public CARD {
public:
  explicit card() : CARD()  {}
public: // pure?
  virtual CARD* clone(CS&){ unreachable(); }
};

std::string command(char *command);
void parse(char *command);


DISPATCHER<CMD>::INSTALL install_command(char *name, CMD*);
DISPATCHER<CARD>::INSTALL install_device(char *name, CARD*);

// maybe later
void uninstall_command(DISPATCHER<CMD>::INSTALL *installer);
