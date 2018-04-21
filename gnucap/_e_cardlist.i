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
%module(directors="0", allprotected="1") e_cardlist

%{
#include <e_cardlist.h>
#include <u_time_pair.h>
%}

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
