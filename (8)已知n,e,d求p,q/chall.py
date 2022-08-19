from gmpy2 import invert
from md5 import md5
from secret import p, q

e = 65537
n = p*q
phi = (p-1)*(q-1)
d = invert(e, phi)

print n, e, d
print "Flag: flag{%s}" %md5(str(p + q)).hexdigest()



