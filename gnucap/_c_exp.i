%module(directors="0", allprotected="1") c_exp

%include <std_string.i>

%{
#include "globals.h"
#include "m_expression.h"
#include "c_comand.h"
#include "e_cardlist.h"
%}

%inline %{

  // void eval_(CS& cmd, CARD_LIST* Scope)
  // {
  //   Expression e(cmd);
  //   cmd.check(bDANGER, "syntax error");
  //   Expression r(e, Scope);
  //   std::cout << e << '=' << r << '\n';
  // }

  double eval(std::string what)
  {
	CS cmd(CS::_STRING, what);
    Expression e(cmd);
    cmd.check(bDANGER, "syntax error");
    Expression r(e, &CARD_LIST::card_list);
    return r.eval();
  }

%}
