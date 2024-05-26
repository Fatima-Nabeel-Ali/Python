d= { }
L1 = ['HTTP','HTTPS','FTP','DNS']
L2 = [80,433,21,53]
for m,f in zip(L1,L2):
    d[m]=f
print(d)