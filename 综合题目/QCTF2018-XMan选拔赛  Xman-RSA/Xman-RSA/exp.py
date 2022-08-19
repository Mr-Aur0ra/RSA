#!/usr/bin/python
#coding:utf-8
#Author@醉清风

import base64
import libnum
import gmpy2
from Crypto.Util.number import long_to_bytes

lines = open('ciphertext','r').readlines()
msg1c1 = int(lines[0],16)
msg2c2 = int(lines[1],16)

lines = open('n2&n3','r').readlines()
n2 = int(base64.b64decode(lines[0]).encode('hex'),16)
n3 = int(base64.b64decode(lines[1]).encode('hex'),16)

lines=open('n1.encrypted','r').readlines()
n1c1 = int(lines[0],16)
n1c2 = int(lines[1],16)

e1 = 0x1001
e2 = 0x101

#使用共模攻击得到n1
_, r, s = gmpy2.gcdext(e1,e2)
n1 = pow(n1c1, r, n3) * pow(n1c2, s, n3) %n3


#n1,n2有一个共同的质因数p12=p1=p2
p12 = gmpy2.gcd(n1, n2)
assert (p12 != 1)   
q1 = n1 / p12
q2 = n2 / p12
e = 0x1001
d1 = gmpy2.invert(e, (p12 - 1) * (q1 - 1))
d2 = gmpy2.invert(e, (p12 - 1) * (q2 - 1))
msg1 = pow(msg1c1, d1, n1)
msg2 = pow(msg2c2, d2, n2)
print long_to_bytes(msg1)+long_to_bytes(msg2)
