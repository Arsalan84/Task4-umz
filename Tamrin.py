import random
while True:
    A={"a1":random.choice([True,False]),"a2":random.choice([True,False]),"a3":random.choice([True,False])}
    B={"b1":random.choice([True,False]),"b2":random.choice([True,False]),"b3":None}
    C={"c1":None,"c2":None,"c3":random.choice([True,False])}
    D={"d1":None,"d2":None,"d3":None}
    corect_count=0
    incorect_count=0
    if A["a1"]==True:
        C.update({"c1":False})
    else:
        C.update({"c1":True})
    if A["a2"]==True:
        B.update({"b3":False})
        C.update({"c2":False})
    else:
        B.update({"b3":True})
        C.update({"c2":True})
    if B["b2"]==True:
        D.update({"d3":False})
    else:
        D.update({"d3":True})
    if C["c3"]==True:
        D.update({"d2":False})
    else:
        D.update({"d2":True})
    if B["b1"]==True:
        D.update({"d1":False})
    else:
        D.update({"d1":True})
    if A["a3"]==False:
        A.update({"a3":True})            
    for i in [A,B,C,D]:
        for j in i:
            if i[j]==True:
                corect_count+=1
            else:
                incorect_count+=1
    
    if incorect_count==6 and corect_count==6:
          print(A,B,C,D)        
          if A["a2"]==True and B["b3"]==False and C["c2"]==False:
               print("the thief is B")
          elif D["d3"]==True and B["b2"]==False:
               print("the thief is A")
          elif D["d1"]==True and B["b1"]==False:
               print("the thief is D")
          else:
               print("the thief is C") 
          break