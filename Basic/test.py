x,y,z="t1 t5 p2".split()
okx=0
oky=0
okz=0
if(x[0]=='s' or x[0]=='t' or x[0]=='p'):
    okx=x[1]
if(y[0]=='s' or y[0]=='t' or y[0]=='p'):
    oky=y[1]
if(z[0]=='s' or z[0]=='t' or z[0]=='p'):
    okz=z[1]

print(okx, oky , okz)