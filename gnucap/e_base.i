
class CKT_BASE {
private:
  mutable int	_probes;		/* number of probes set */
  std::string	_label;
public:
  //static SIM_DATA* _sim;
  //static PROBE_LISTS* _probe_lists;
  //--------------------------------------------------------------------
protected: // create and destroy
  explicit CKT_BASE()			  :_probes(0), _label() {}
  explicit CKT_BASE(const std::string& s) :_probes(0), _label(s) {}
  explicit CKT_BASE(const CKT_BASE& p)	  :_probes(0), _label(p._label) {}
  virtual  ~CKT_BASE();
};
