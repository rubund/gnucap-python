
%include e_base.i

class CARD : public CKT_BASE {
protected:                              // create and destroy.
private:
  CARD();
  CARD(const CARD&);
public:
  virtual  ~CARD()                      {delete _subckt;}

public: // parameters
  virtual std::string value_name()const = 0;

  virtual bool param_is_printable(int)const;
  virtual std::string param_name(int)const;
  virtual std::string param_name(int,int)const;
  virtual std::string param_value(int)const;
  virtual void set_param_by_name(std::string, std::string);
  virtual void set_param_by_index(int, std::string&, int);
  virtual int param_count()const {return 0;}
};
