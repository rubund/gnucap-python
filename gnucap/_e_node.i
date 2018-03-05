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
%module(directors="0", allprotected="1") e_node

%{
#include <e_node.h>
%}

class node_t {
public:
  int	m_()const;
  int t_()const;
  int	e_()const;
//  NODE* n_(); not yet.

  const std::string  short_label()const;
  void	set_to_ground(CARD*);
  void	new_node(const std::string&, const CARD*);
  void	new_model_node(const std::string& n, CARD* d);
  void	map_subckt_node(int* map_array, const CARD* d);
  bool	is_grounded()const;
  bool	is_connected()const;

  // node_t& map(); name conflict

  explicit node_t();
  node_t(const node_t&);
  explicit    node_t(NODE*);
  ~node_t() {}

public:
  //LOGIC_NODE&	    operator*()const	{untested();return data();}
  LOGIC_NODE*	    operator->()	{return &data();}

  // node_t& operator=(const node_t& p); // yikes.

  bool operator==(const node_t& p);

public:
  double      v0()const;
  COMPLEX     vac()const;
  double&     i();
  //COMPLEX&    iac();
};

%{

struct nodearray_t {
  operator node_t const*() const { return _t; }
  operator node_t*() { return _t; }
  node_t const& get(unsigned i) const{return _t[i];}
//private: // why not?
  node_t* _t;
};

%}

struct nodearray_t {
  node_t* _t;
//  node_t const& get(unsigned i) const;
};

%inline %{

node_t& get_node(node_t* n, unsigned x){
return n[x];
}

%}


%extend nodearray_t {
  // inline size_t __len__() const { return -1; }
  inline const node_t& __getitem__(size_t i) const{
    return self->get(i);
  }
  // inline void __setitem__ ...
}
