from __future__ import annotations
def run(x):
 from collections import Counter
 c=Counter()
 def walk(v):
  c["null" if v is None else "boolean" if isinstance(v,bool) else "number" if isinstance(v,(int,float)) else "string" if isinstance(v,str) else "array" if isinstance(v,list) else "object"]+=1
  if isinstance(v,dict): [walk(z) for z in v.values()]
  elif isinstance(v,list): [walk(z) for z in v]
 walk(x)
 return dict(c)
