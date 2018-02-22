#include <c_comand.h>
#include <l_dispatcher.h>
#include <s__.h>

class SIMWrapper : public SIM {
public:
  explicit SIMWrapper():SIM()  {}
  virtual void  setup(CS&)=0;
  virtual void  sweep()=0;
  virtual void  do_it(CS&, CARD_LIST*){ incomplete();
  };
};

std::string command(char *command);
void parse(char *command);
DISPATCHER<CMD>::INSTALL *attach_command(char *command_name, CMD *cmd);
void detach_command(DISPATCHER<CMD>::INSTALL *installer);

