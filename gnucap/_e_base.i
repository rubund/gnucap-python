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
%module(directors="0", allprotected="1") e_base
%feature(nodirector) CKT_BASE;

%include _m_wave.i
%include std_string.i
%{
#include <e_base.h>
%}

class CKT_BASE {
private:
  mutable int	_probes;		/* number of probes set */
  std::string	_label;
public:
  //static SIM_DATA* _sim;
  //static PROBE_LISTS* _probe_lists;
  //--------------------------------------------------------------------
protected: // create and destroy
  explicit CKT_BASE()			  :_probes(0), _label() { untested(); }
  explicit CKT_BASE(const std::string& s) :_probes(0), _label(s) { untested(); }
  explicit CKT_BASE(const CKT_BASE& p)	  :_probes(0), _label(p._label) { untested(); }
  virtual  ~CKT_BASE();
public:
  static WAVE* find_wave(const std::string&);
};
