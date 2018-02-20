#include "wrap.h"
#include <u_lang.h>
#include <c_comand.h>
#include <globals.h>
#include <m_wave.h>
#include <u_prblst.h>
#include <u_sim_data.h>
#include <s__.h>
#include <io_.h>
#include <e_cardlist.h>

#include "numpy_interface.h"

#include <stdio.h>
#include <string>
#include <fstream>

std::string command(char *command)
{
	trace1("command", command);
  
  char filename[L_tmpnam];
  
  tmpnam(filename);
  
  // supress output to stdout
//  IO::mstdout.detach(stdout);

  // send output to file
//   CMD::command(std::string("> ") + std::string(filename), &CARD_LIST::card_list);

  CMD::command(std::string(command), &CARD_LIST::card_list);

//  CMD::command(">", &CARD_LIST::card_list);

  // Open file an read it
  std::ifstream ifs(filename);

  std::ostringstream oss;

  oss << ifs.rdbuf();

  std::string output(oss.str());

  unlink(filename);
  
  return output;
}

DISPATCHER<CMD>::INSTALL *attach_command(char *command_name, CMD *cmd) {
  return new DISPATCHER<CMD>::INSTALL(&command_dispatcher, command_name, cmd);
}

void detach_command(DISPATCHER<CMD>::INSTALL *installer) {
  delete installer;
}

struct defpl_load{
	defpl_load(){ untested();
  // prepare_env();
  CKT_BASE::_sim = new SIM_DATA;
  CKT_BASE::_probe_lists = new PROBE_LISTS;
		//void* handle=dlopen("/usr/local/lib/libgnucap.so", RTLD_GLOBAL | RTLD_NOW) ;
		//std::cerr << dlerror() <<"\n";
		//trace1("dlopened", handle);
		// try{
		//   CMD::command("load /usr/local/lib/gnucap/gnucap-default-plugins.so", &CARD_LIST::card_list);
		//   CMD::command("load /usr/local/lib/gnucap/gnucap-default-plugins.so", &CARD_LIST::card_list);
		// }catch(Exception& e){ untested();
		// 	std::cout << e.message();
		// }

	}
}l1;
