
%{
#include "wrap.h"
%}

%{


%}


%extend COMPLEX_array_t {
  // inline size_t __len__() const { return status.something }
  inline COMPLEX& __getitem__(size_t i){
    return self->get(i);
  }
}

