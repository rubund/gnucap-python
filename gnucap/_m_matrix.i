// Copyright: ..  -2017 Albert Davis
//            2009-2011 Henrik Johansson
//            2018 Felix Salfelder
// Author: Albert Davis
// License: GPLv3
/*
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
//  void          fbsub(T* v) const;
  void          fbsub(T* x, const T* b, T* c = NULL) const;

  T     d(int r, int  )const    {return *(_diaptr[r]);}
 //  const T&    s(int r, int c);

private:
  T& m(int r, int c);
};

%template(BSMATRIXd) BSMATRIX<double>;
%template(BSMATRIXc) BSMATRIX<COMPLEX>;

class BSCR{
  BSCR( BSMATRIX<COMPLEX> const& m, size_t r) : _m(m), _r(r){ }
private:
  BSMATRIX<COMPLEX>& _m;
  size_t r;
};

%extend BSMATRIX<COMPLEX> {
  void fbsub_(COMPLEX_array_t& x){
    return self->fbsub(x._t);
  }
  inline std::string __repr__(){
        return("BMATRIX: incomplete");
  }
  inline BSCR __getitem__(int p){
    return BSCR(*self, p);
//    return self->s(p,p);
  }
}

%extend BSCR{
  inline COMPLEX __getitem__(int p){
    return self->get(p);
  }
  inline std::string __repr__(){
        return("BSCR: incomplete");
  }

  void __getitem__(PyObject *param) {
    if (PySlice_Check(param)) {
      incomplete();
      Py_ssize_t len = -1u, start = 0, stop = 0, step = 0, slicelength = 0;

      PySlice_GetIndicesEx((PySliceObject*)param,
          len, &start, &stop, &step, &slicelength);
      trace5("slice", len, start, stop, step, slicelength);
    }else{
    }
  }
}

