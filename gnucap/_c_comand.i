/* Copyright (C) 2018 Felix Salfelder
 * Author: Felix Salfelder <felix@salfelder.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 *------------------------------------------------------------------
 */
%module(directors="0", allprotected="1") c_comand

// .h?
%include _e_base.i

%{
#include <c_comand.h>
%}

class CMD : public CKT_BASE {
public:
  std::string value_name()const {return "";}
  virtual void do_it(CS&, CARD_LIST*) = 0;
  virtual ~CMD() {}
  static  void  cmdproc(CS&, CARD_LIST*);
  static  void	command(const std::string&, CARD_LIST*);
};

