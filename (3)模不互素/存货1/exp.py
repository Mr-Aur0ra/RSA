#!/usr/bin/python
#coding:utf-8
#@Author:醉清风

import gmpy2
from Crypto.Util.number import long_to_bytes

lines = open('tmp.txt','r').readlines()

c1 = int(lines[2],16)
c2 = int(lines[6],16)
n1 = int(lines[0])
n2 = int(lines[4])

p12 = gmpy2.gcd(n1, n2)
assert (p12 != 1)
q1 = n1 / p12
q2 = n2 / p12
e = 0x10001
d1 = gmpy2.invert(e, (p12 - 1) * (q1 - 1))
d2 = gmpy2.invert(e, (p12 - 1) * (q2 - 1))
m1 = pow(c1, d1, n1)
m2 = pow(c2, d2, n2)
print long_to_bytes(m1)+long_to_bytes(m2)
